'''
Epidemic modelling

Temurmalik Kudratov

Functions for running a simple epidemiological simulation
'''

import click

# This seed should be used for debugging purposes only!  Do not refer
# to it in your code.
TEST_SEED = 20170217


def count_infected(city):


    # YOUR CODE HERE

    # REPLACE -1 WITH THE APPROPRIATE INTEGER

    return len([x for x in city if x.startswith("I")])


def has_an_infected_neighbor(city, position):

    # This function should only be called when the person at position
    # is susceptible to infection.
    assert city[position] == "S"

    # YOUR CODE HERE

    # my_var for listings them
    if len(city) == 0 or len(city) == 1:
        return False
    if position == 0:
        return city[position + 1].startswith("I")
    elif position == len(city) - 1:
        return city[position - 1].startswith("I")
    else:
        return (city[position + 1].startswith("I") or city[position - 1].startswith("I"))
    # else:
    #     return (city[position+1].startswith("I") or city[position-1].startswith("I"))


def advance_person_at_position(city, position, days_contagious):

    if city[position] == "V":
        return "V"

    if city[position].startswith("I"):
        if int(city[position][1:]) + 1 == days_contagious:
            return "R"

        elif int(city[position][1:]) + 1 < days_contagious:
            return f"I{int(city[position][1:]) + 1}"

    elif city[position].startswith("S") and not has_an_infected_neighbor(city, position):
        return "S"
    elif city[position].startswith("S") and has_an_infected_neighbor(city, position):
        return "I0"
    elif city[position].startswith("R"):
        return "R"
    elif int(city[position][1:]) + 1 < days_contagious:
        return f"I{int(city[position][1:]) + 1}"
    else:
        return "R"


def simulate_one_day(starting_city, days_contagious):


    # YOUR CODE HERE

    # REPLACE None WITH THE APPROPRIATE LIST OF STRINGS
    return [advance_person_at_position(starting_city, position, days_contagious) for position, _ in
            enumerate(starting_city, start=0)]


def run_simulation(starting_city, days_contagious,
                   random_seed=None, vaccine_effectiveness=0.0):

    random.seed(random_seed)
    starting_city = vaccinate_city(starting_city, vaccine_effectiveness)

    n = 0
    while 0 != count_infected(city=starting_city):
        starting_city = simulate_one_day(starting_city=starting_city, days_contagious=days_contagious)
        n += 1

    return (starting_city, n)


def vaccinate_city(starting_city, vaccine_effectiveness):

    new_city = starting_city[:]
    for index, person in enumerate(starting_city):

        if person == "S":
            if vaccine_effectiveness >= random.random():
                new_city[index] = "V"

    print(new_city)
    return new_city


def calc_avg_days_to_zero_infections(
        starting_city, days_contagious,
        random_seed, vaccine_effectiveness,
        num_trials):

    assert num_trials > 0
    total = 0
    for i in range(num_trials):
        total += run_simulation(starting_city, days_contagious, random_seed, vaccine_effectiveness)[1]
        if i >= 1:
            random_seed += 1

    return total / num_trials

    # REPLACE -1.0 WITH THE APPROPRIATE FLOATING POINT VALUE
    return -1.0


