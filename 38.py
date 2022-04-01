def many(*args, **kwargs):
    print(args)
    print(kwargs)


many(1, 2, 3, 'hello', name='Make', job='developer')
