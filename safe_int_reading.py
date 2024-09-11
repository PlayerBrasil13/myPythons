def read_int(prompt, min, max):
    try:
        int_input =  int(input(prompt))
        assert min <= int_input and max >= int_input
        return str(int_input)
    except ValueError:
        print("Error: wrong input")
        return read_int(prompt, min, max)
    except AssertionError:
        print("Error: the value is not within permitted range (", min, "..", max, ")", sep="")
        return read_int(prompt, min, max)


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
