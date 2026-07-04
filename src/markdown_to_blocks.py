def markdown_to_blocks(markdown: str) -> list[str]:
    """
    Convert markdown to blocks of text.
    """
    blocks = []
    current_block = []
    for line in markdown.splitlines():
        line = line.strip()
        if line == "":
            if current_block:
                blocks.append("\n".join(current_block))
                current_block = []
        else:
            current_block.append(line)
    if current_block:
        blocks.append("\n".join(current_block))
    return blocks
