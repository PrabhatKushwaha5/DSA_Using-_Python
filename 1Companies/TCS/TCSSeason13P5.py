import re

def parse_command(cmd):
    widths = {'even': 75, 'odd': 75}
    hyphen = False
    tokens = cmd.split()
    i, n = 0, len(tokens)
    while i < n:
        if tokens[i] == '-w':
            widths['even'] = widths['odd'] = int(tokens[i+1])
            i += 2
        elif tokens[i] == '-w-e':
            widths['even'] = int(tokens[i+1])
            i += 2
        elif tokens[i] == '-w-o':
            widths['odd'] = int(tokens[i+1])
            i += 2
        elif tokens[i] == 'h':
            hyphen = True
            i += 1
        else:
            i += 1
    return widths, hyphen

def is_url_or_email(word):
    return word.startswith("http://") or word.startswith("https://") or '@' in word

def split_word(word, space_left):
    if space_left <= 1:
        return word, None
    cut = space_left - 1
    return word[:cut] + '-', word[cut:]

def clean_markdown_links(text):
    md_link_pattern = re.compile(r'\[([^\]]+)\]\((?:mailto:)?([^\)]+)\)')
    return md_link_pattern.sub(r'\2', text)

def force_bullets_newline(text):
    # Insert newline before bullets, bullets are *, -, or numbers with . or )
    # Only if not already start of line
    return re.sub(r'(?<!^)(\s+)(\*|[-]|[0-9]+[.)])', r'\n\2', text)

def format_paragraph(words, widths, hyphen):
    res = []
    line = ''
    line_count = 0
    for word in words:
        width = widths['even'] if line_count % 2 == 0 else widths['odd']
        if not line:
            line = word
        else:
            if len(line) + 1 + len(word) <= width:
                line += ' ' + word
            else:
                if hyphen and not is_url_or_email(word) and len(word) > (width - len(line) - 1):
                    space_left = width - len(line)
                    part1, part2 = split_word(word, space_left)
                    line += ' ' + part1
                    res.append(line)
                    line_count += 1
                    line = part2 or ''
                else:
                    res.append(line)
                    line_count += 1
                    line = word
    if line:
        res.append(line)
    return res

def text_formatter(N, lines, cmd):
    widths, hyphen = parse_command(cmd)
    paragraphs = []
    current = []
    for line in lines:
        if line.strip() == '':
            if current:
                paragraphs.append(' '.join(current))
                current = []
        else:
            current.append(line.strip())
    if current:
        paragraphs.append(' '.join(current))

    # Clean Markdown links and force bullets new lines in each paragraph
    clean_paras = []
    for para in paragraphs:
        para = clean_markdown_links(para)
        para = force_bullets_newline(para)
        clean_paras.append(para)
    paragraphs = clean_paras

    final_lines = []
    for para in paragraphs:
        # Split paragraph on new lines forced by bullets
        parts = para.split('\n')
        for part in parts:
            part = part.strip()
            if not part:
                continue
            is_bullet = re.match(r'^(\*|[-]|[0-9]+[.)])(\s|$)', part)
            if is_bullet:
                # Separate bullet and rest of line
                tokens = part.split(None, 1)
                bullet = tokens[0]
                rest = tokens[1] if len(tokens) > 1 else ''
                if rest:
                    formatted_rest = format_paragraph(rest.split(), widths, hyphen)
                    # Attach bullet to first line, print rest fully
                    first_line = bullet + ' ' + formatted_rest[0]
                    final_lines.append(first_line)
                    final_lines.extend(formatted_rest[1:])
                else:
                    final_lines.append(bullet)
            else:
                words = part.split()
                final_lines.extend(format_paragraph(words, widths, hyphen))
        final_lines.append('')  # paragraph break

    while final_lines and final_lines[-1] == '':
        final_lines.pop()

    return '\n'.join(final_lines)

# ---------------- Driver Code ----------------
if __name__ == "__main__":
    N = int(input().strip())
    lines = [input() for _ in range(N)]
    cmd = input().strip()
    result = text_formatter(N, lines, cmd)
    print(result)
