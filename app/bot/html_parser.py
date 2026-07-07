from bs4 import BeautifulSoup, NavigableString, Tag


def html_to_telegram(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")

    result = []

    def walk(node):
        if isinstance(node, NavigableString):
            text = str(node).strip()
            if text:
                result.append(text)

        elif isinstance(node, Tag):

            match node.name:

                case "p":
                    for child in node.children:
                        walk(child)
                    result.append("\n\n")

                case "br":
                    result.append("\n")

                case "ul":
                    for child in node.children:
                        walk(child)
                    result.append("\n")

                case "li":
                    result.append("• ")
                    for child in node.children:
                        walk(child)
                    result.append("\n")

                case "b" | "strong":
                    result.append("<b>")
                    for child in node.children:
                        walk(child)
                    result.append("</b>")

                case "i" | "em":
                    result.append("<i>")
                    for child in node.children:
                        walk(child)
                    result.append("</i>")

                case "a":
                    href = node.get("href", "")
                    result.append(f'<a href="{href}">')
                    for child in node.children:
                        walk(child)
                    result.append("</a>")

                case _:
                    for child in node.children:
                        walk(child)

    walk(soup)

    text = "".join(result)

    while "\n\n\n" in text:
        text = text.replace("\n\n\n", "\n\n")

    return text.strip()