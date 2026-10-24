def decode(s):
    result = ''
    i = 0
    while i < len(s):
        if s[i].isdigit():
            result += s[i + 1] * int(s[i])
            i += 2
        else:
            result += s[i]
            i += 1
    return result


def read_sequences(filename):
    proteins = {}
    with open(filename, encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\r\n')
            parts = line.split('\t')
            if len(parts) < 3:
                continue
            name = parts[0]
            organism = parts[1]
            sequence = decode(parts[2])
            proteins[name] = (organism, sequence)
    return proteins


def read_commands(filename):
    commands = []
    with open(filename, encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\r\n')
            if line.strip() == '':
                continue
            commands.append(line.split('\t'))
    return commands


def search(proteins, sequence):
    found = []
    for name, (organism, seq) in proteins.items():
        if sequence in seq:
            found.append((organism, name))
    return found


def diff(seq1, seq2):
    count = abs(len(seq1) - len(seq2))
    for a, b in zip(seq1, seq2):
        if a != b:
            count += 1
    return count


def mode(seq):
    best = ''
    best_count = 0
    for ch in sorted(set(seq)):
        c = seq.count(ch)
        if c > best_count:
            best = ch
            best_count = c
    return best, best_count


def main():
    proteins = read_sequences('sequences.txt')
    commands = read_commands('commands.txt')
    line = '-' * 80

    with open('genedata.txt', 'w', encoding='utf-8') as out:
        out.write('Vladislav Gaidukov\n')
        out.write('Genetic Searching\n')
        out.write(line + '\n')

        for i, cmd in enumerate(commands, 1):
            num = '{:03d}'.format(i)
            op = cmd[0]

            if op == 'search':
                sequence = decode(cmd[1])
                out.write(num + '\tsearch\t' + sequence + '\n')
                out.write('organism\t\t\tprotein\n')
                found = search(proteins, sequence)
                if not found:
                    out.write('NOT FOUND\n')
                else:
                    for organism, name in found:
                        out.write(organism + '\t\t' + name + '\n')

            elif op == 'diff':
                name1 = cmd[1]
                name2 = cmd[2]
                out.write(num + '\tdiff\t' + name1 + '\t' + name2 + '\n')
                out.write('amino-acids difference:\n')
                missing = []
                if name1 not in proteins:
                    missing.append(name1)
                if name2 not in proteins:
                    missing.append(name2)
                if missing:
                    out.write('MISSING: ' + ', '.join(missing) + '\n')
                else:
                    seq1 = proteins[name1][1]
                    seq2 = proteins[name2][1]
                    out.write(str(diff(seq1, seq2)) + '\n')

            elif op == 'mode':
                name = cmd[1]
                out.write(num + '\tmode\t' + name + '\n')
                out.write('amino-acid occurs:\n')
                if name not in proteins:
                    out.write('MISSING: ' + name + '\n')
                else:
                    ch, count = mode(proteins[name][1])
                    out.write(ch + '\t\t' + str(count) + '\n')

            out.write(line + '\n')


main()
