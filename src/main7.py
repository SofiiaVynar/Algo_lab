def longest_chain(words):
    words_set = set(words)
    chains = {}
    max_chain_length = 0
    total_iterations = 0

    for word in words:
        curr_word = word
        chain_words = [word]
        chain_length = 1

        while len(curr_word) > 1:
            possible_words = [curr_word[:i] + curr_word[i + 1:] for i in range(len(curr_word))]
            filter_words = [included_words for included_words in possible_words if included_words in words_set]
            total_iterations += 1

            if not filter_words:
                break

            max_length = 0
            for included_words in filter_words:
                if len(included_words) > max_length:
                    max_length = len(included_words)
                    curr_word = included_words
                    chain_words.append(included_words)
                    total_iterations += 1


            chain_length += 1
            total_iterations += 1

        if chain_length > max_chain_length:
            max_chain_length = chain_length
            total_iterations += 1

        if chain_length not in chains:
            chains[chain_length] = []
            total_iterations += 1


        chains[chain_length].append(chain_words)

    return max_chain_length, chains, total_iterations


with open('../wchain.in', 'r') as file:
    content = file.readlines()

    if len(content) < 2:
        print("Неправильний формат файлу: відсутні дані про кількість слів.")
    else:
        N = int(content[0].strip())
        words = [word.strip() for word in content[1:]]

        if N != len(words):
            print("Неправильна кількість слів у файлі.")

        for word in words:
            if not (1 <= len(word) <= 50 and word.islower() and all('a' <= char <= 'z' for char in word)):
                print("Слова мають складатися лише з малих латинських літер від a до z.")
                break
        else:
            result_length, result_chains, result_iter = longest_chain(words)

            with open('../wchain.out', 'w') as output_file:
                output_file.write(f"{result_length}\n")
                for chain_length, chains in result_chains.items():
                    if chain_length == result_length:
                        for chain in chains:
                            output_file.write('->'.join(chain) + '\n')
                output_file.write(f"{result_iter}\n")
