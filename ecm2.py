# speed of light in Km/s
C = 299792.458

def compute_e(mass:float) -> float:
    '''
    Computes Einstein's equation of Energy when recieving as input
    the mass of the object in Kg.
    '''
    answer = mass * (convert_speed_2_m(C)**2)
    return answer

def convert_speed_2_m(speed_in_km:float) -> float:
    '''
    Translates speed in Km/s to m/s, providede that the input is given in Km/s.
    '''
    return (speed_in_km * 1000)

def my_printer(mass:float, results:float) -> None:
    '''
    Printin one line the mass of the object in Kg. -which is a parameter, and the
    computation of Energy in Joules.
    '''
    print(f"An object of mass {mass:.2f} will result in Energy being equal to {results:.8e} Joules")

def main() -> None:
    '''
    Orchestrate reading the input data from the terminal an calling the appropriate functions to do the job.
    '''
    mass = float(input("Please provide the mass of the object in Kg ==> "))
    results = compute_e(mass)
    my_printer(mass, results)

main()
