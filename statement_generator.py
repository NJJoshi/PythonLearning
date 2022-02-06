def statement_generator(subjects, verbs, objects):
    result_statements = []
    for subject in subjects:
        for verb in verbs:
            for obj in objects:
                result_statements.append(subject + " " + verb + " " + obj)
    return result_statements


def main():
    subjects = ["I", "You"]
    verbs = ["Play", "Love"]
    objects = ["Hockey", "Football"]

    result_statements = statement_generator(subjects, verbs, objects)

    print('Final result:', result_statements)


main()
