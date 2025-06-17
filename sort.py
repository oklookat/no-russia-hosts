import re

def process_domains_with_inline_comments(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    domain_map = {}
    comment_buffer = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

        if stripped.startswith('#'):
            # Строка-комментарий над доменом
            comment_buffer.append(line.rstrip('\n'))
            continue

        # Обрабатываем строку с доменом и возможным инлайн-комментарием
        # Разделим домен и комментарий (если есть)
        match = re.match(r'^([^\s#]+)(\s*#.*)?$', stripped)
        if match:
            domain = match.group(1).strip()
            inline_comment = match.group(2).strip() if match.group(2) else None

            block = []
            if comment_buffer:
                block.extend(comment_buffer)
                comment_buffer = []

            if inline_comment:
                block.append(f"{domain} {inline_comment}")
            else:
                block.append(domain)

            domain_map[domain] = block  # сохраняем, перезаписывая при повторе

    # Сортируем по домену
    sorted_blocks = [domain_map[domain] for domain in sorted(domain_map)]

    # Пишем в файл
    with open(output_file, 'w', encoding='utf-8') as f:
        for block in sorted_blocks:
            for line in block:
                f.write(line + '\n')

# Пример использования
process_domains_with_inline_comments('hosts.txt', 'hosts.txt')