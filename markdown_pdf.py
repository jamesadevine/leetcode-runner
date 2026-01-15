# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "markdown",
#     "xhtml2pdf",
# ]
# ///

import argparse
import re
from markdown import markdown
from xhtml2pdf import pisa
from pathlib import Path


def fix_code_blocks_for_pdf(html: str) -> str:
    """Convert newlines in <pre> blocks to <br/> for xhtml2pdf compatibility."""

    def replace_pre_content(match):
        content = match.group(1)
        # Replace newlines with <br/> and spaces with &nbsp;
        content = content.replace("\n", "<br/>")
        # Preserve leading spaces on each line
        lines = content.split("<br/>")
        fixed_lines = []
        for line in lines:
            # Count leading spaces and convert to &nbsp;
            stripped = line.lstrip(" ")
            leading_spaces = len(line) - len(stripped)
            fixed_lines.append("&nbsp;" * leading_spaces + stripped)
        return "<pre><code>" + "<br/>".join(fixed_lines) + "</code></pre>"

    # Match <pre><code>...</code></pre> blocks
    html = re.sub(
        r"<pre><code[^>]*>(.*?)</code></pre>",
        replace_pre_content,
        html,
        flags=re.DOTALL,
    )

    # Also handle bare <pre> blocks without <code>
    def replace_bare_pre(match):
        content = match.group(1)
        content = content.replace("\n", "<br/>")
        lines = content.split("<br/>")
        fixed_lines = []
        for line in lines:
            stripped = line.lstrip(" ")
            leading_spaces = len(line) - len(stripped)
            fixed_lines.append("&nbsp;" * leading_spaces + stripped)
        return "<pre>" + "<br/>".join(fixed_lines) + "</pre>"

    html = re.sub(r"<pre>(?!<code)(.*?)</pre>", replace_bare_pre, html, flags=re.DOTALL)

    return html


def convert_markdown_to_pdf(input_path: str, output_path: str | None = None) -> None:
    """Convert a markdown file to PDF."""
    input_file = Path(input_path)

    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    if output_path is None:
        output_path = str(input_file.with_suffix(".pdf"))

    # Read markdown content
    md_content = input_file.read_text(encoding="utf-8")

    # Convert markdown to HTML
    html_content = markdown(
        md_content, extensions=["tables", "fenced_code", "codehilite"]
    )

    # Fix code blocks for xhtml2pdf compatibility
    html_content = fix_code_blocks_for_pdf(html_content)

    # Wrap in full HTML with CSS
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            @page {{
                margin: 1.5cm;
            }}
            body {{
                font-family: Helvetica, Arial, sans-serif;
                font-size: 10pt;
                line-height: 1.4;
            }}
            h1 {{ font-size: 20pt; border-bottom: 2px solid #333; padding-bottom: 6px; }}
            h2 {{ font-size: 16pt; border-bottom: 1px solid #666; padding-bottom: 4px; margin-top: 20px; }}
            h3 {{ font-size: 12pt; margin-top: 16px; }}
            table {{ border-collapse: collapse; width: 100%; margin: 12px 0; font-size: 8pt; }}
            th, td {{ border: 1px solid #ddd; padding: 5px; text-align: left; }}
            th {{ background-color: #f5f5f5; font-weight: bold; }}
            code {{
                font-family: Courier;
                font-size: 9pt;
                background-color: #f0f0f0;
                padding: 1px 3px;
            }}
            pre {{
                background-color: #f4f4f4;
                border: 1px solid #ddd;
                border-radius: 4px;
                padding: 10px;
                margin: 10px 0;
                font-family: Courier;
                font-size: 8pt;
                line-height: 1.3;
                white-space: pre-wrap;
                word-wrap: break-word;
            }}
            pre code {{
                background-color: transparent;
                padding: 0;
                font-size: 8pt;
            }}
            .codehilite {{
                background-color: #f4f4f4;
                border: 1px solid #ddd;
                border-radius: 4px;
                padding: 10px;
                margin: 10px 0;
            }}
            .codehilite pre {{
                margin: 0;
                padding: 0;
                border: none;
                background: transparent;
            }}
            hr {{ border: none; border-top: 1px solid #ddd; margin: 16px 0; }}
            ul, ol {{ padding-left: 20px; }}
            li {{ margin: 3px 0; }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    # Generate PDF
    with open(output_path, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(full_html, dest=pdf_file)

    if pisa_status.err:
        raise RuntimeError(f"PDF generation failed with {pisa_status.err} errors")

    print(f"PDF created: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Markdown to PDF")
    parser.add_argument("input", help="Input markdown file path")
    parser.add_argument(
        "-o", "--output", help="Output PDF file path (default: same name as input)"
    )

    args = parser.parse_args()
    convert_markdown_to_pdf(args.input, args.output)
