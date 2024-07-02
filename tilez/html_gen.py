def create_html_with_css_and_divs(txt_file_path, output_html_path):
    with open(txt_file_path, 'r') as file:
        filenames = file.read().splitlines()

    css_rules = []
    div_elements = []

    for filename in filenames:
        filename_without_ext = filename.rsplit('.', 1)[0]
        css_rules.append(f"""
        .{filename_without_ext} {{
            background-image: url('{filename}');
            height: 100vh;
            width: 100vw;
        }}
        """)
        div_elements.append(f'<div class="{filename_without_ext}"></div>')

    css_content = '\n'.join(css_rules)
    div_content = '\n'.join(div_elements)

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Image Backgrounds</title>
        <style>
        {css_content}
        </style>
    </head>
    <body>
        {div_content}
    </body>
    </html>
    """

    with open(output_html_path, 'w') as output_file:
        output_file.write(html_content)

    print(f'HTML file has been created at {output_html_path}')

# Example usage
txt_file_path = 'sorted_filenames.txt'
output_html_path = 'output.html'
create_html_with_css_and_divs(txt_file_path, output_html_path)
