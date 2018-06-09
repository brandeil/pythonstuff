def make_pizza(size, *toppings):
    """ Make a pizza """
    print("\nmaking a {0} pizza".format(size))
    print("toppings")
    for topping in toppings:
        print('- '+topping)
        