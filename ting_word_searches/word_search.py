def exists_word(word, instance):
    result = list()

    for i in range(len(instance)):
        search_word_file = dict()
        data_file = instance.search(i)
        phrases = data_file["linhas_do_arquivo"]
        occurrences = list()
        for j, phrase in enumerate(phrases, start=1):
            if word.lower() in phrase.lower():
                occurrences.append({"linha": j})

        if occurrences:
            search_word_file["palavra"] = word
            search_word_file["arquivo"] = data_file["nome_do_arquivo"]
            search_word_file["ocorrencias"] = occurrences
            result.append(search_word_file)

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
