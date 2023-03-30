kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    'C': 'Dennis Ritchie',
}

if __name__ == "__main__":
    line = '\n'.join('{} was created by {}'.format(key, value)
                     for key, value in kata.items())
    print(line)
