def test_function(x):
    def inner_function(x):
        print("Я в области видимости test_function")
    inner_function()


inner_function()



