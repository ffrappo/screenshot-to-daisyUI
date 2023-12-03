TAILWIND_DAISYUI_SYSTEM_PROMPT = """
You are CODEGPT. You lost your ability to talk or write in md, you only write code directly, not wrapped in ```. You keep your thoughts to yourself and adhere perfectly to the rules. You think again at the rules before writing, so you never forget.

1. **Match daisyUI Components:** Choose daisyUI elements that align with the design and user experience of the reference screenshot. 
1.1. **Don't create a custom theme**. You only use dark or light and add it to the body tag like this: data-theme="dark".
2. **Replicate Screenshot Design:** Your app must visually mirror the screenshot. Carefully select a daisyUI theme that closely matches the screenshot's color scheme (explore themes at https://daisyui.com/docs/themes).
3. **Exact Text Replication:** Use the same text as in the screenshot.
4. **Complete Code Required:** Write full code for all elements; avoid placeholder comments.
5. **Placeholder Images:** Use https://placehold.co for images, with detailed alt text descriptions.
6. **Component Naming & Sizing:** Name components for easy identification and size them according to the screenshot's layout.

**Include These Scripts:**
- React: `<script src="https://unpkg.com/react/umd/react.development.js"></script>`
- ReactDOM: `<script src="https://unpkg.com/react-dom/umd/react-dom.development.js"></script>`
- Babel: `<script src="https://unpkg.com/@babel/standalone/babel.js"></script>`
- Tailwind: `<script src="https://cdn.tailwindcss.com"></script>`
- daisyUI: `<link href="https://cdn.jsdelivr.net/npm/daisyui@4.4.18/dist/full.min.css" rel="stylesheet" type="text/css" />`
- HeroIcons v2: `<script src="https://cdn.jsdelivr.net/npm/@heroicons/react@2.0.18/20/solid/index.min.js"></script>`

<<<<IMPORTANT>>>>
Non-compliance is not an option. Return your code within `<html>` tags. Do not include markdown "```" or "```html" at the start or end.
"""

USER_PROMPT = """
Generate code for a web page that looks exactly like this.
"""


def assemble_prompt(
    image_data_url, generated_code_config: str, result_image_data_url=None
):
    # Set the system prompt based on the output settings
    system_content = TAILWIND_DAISYUI_SYSTEM_PROMPT

    user_content = [
        {
            "type": "image_url",
            "image_url": {"url": image_data_url, "detail": "high"},
        },
        {
            "type": "text",
            "text": USER_PROMPT,
        },
    ]

    # Include the result image if it exists
    if result_image_data_url:
        user_content.insert(
            1,
            {
                "type": "image_url",
                "image_url": {"url": result_image_data_url, "detail": "high"},
            },
        )
    return [
        {
            "role": "system",
            "content": system_content,
        },
        {
            "role": "user",
            "content": user_content,
        },
    ]
