import math

# Conversion factors and constants
JOULES_TO_KJ = 0.001
LITERS_ATM_TO_JOULES = 101.325

def heat_of_reaction(known_enthalpies, reaction_heat, coefficients):
    """
    Calculate the heat of formation for an unknown reactant/product.
    """
    total_known_enthalpy = 0
    unknown_component = None

    for component, heat in known_enthalpies.items():
        coeff = coefficients.get(component, 0)
        if heat is None:
            unknown_component = component
        else:
            total_known_enthalpy += coeff * heat

    if unknown_component:
        unknown_heat = (reaction_heat - total_known_enthalpy) / coefficients[unknown_component]
        return unknown_component, unknown_heat
    else:
        return "All enthalpies are known; nothing to calculate."


def work_done_external_pressure(pressure, v_initial, v_final):
    """
    Calculate work done under constant external pressure.
    """
    delta_v = v_final - v_initial
    work = -pressure * delta_v * LITERS_ATM_TO_JOULES  # Work in Joules
    return work * JOULES_TO_KJ  # Convert to kJ


def reversible_work(n_moles, t_kelvin, v_initial, v_final):
    """
    Calculate reversible work during isothermal expansion/compression.
    """
    R = 8.314  # J/(mol*K), ideal gas constant
    work = -n_moles * R * t_kelvin * math.log(v_final / v_initial)
    return work * JOULES_TO_KJ  # Convert to kJ


def sensible_heat_constant_pressure(heat_released, internal_energy_change):
    """
    Calculate sensible heat at constant pressure.
    """
    enthalpy_change = internal_energy_change + heat_released
    return enthalpy_change * JOULES_TO_KJ  # Convert to kJ


def percent_decrease_heat(initial_heat, absorbed_heat):
    """
    Calculate percent decrease in heat.
    """
    decrease = initial_heat - absorbed_heat
    percent_decrease = (decrease / initial_heat) * 100
    return round(percent_decrease, 2)


def main():
    while True:
        print("\nChemistry Problem Calculator")
        print("1. Heat of Reaction (Unknown Heat of Formation)")
        print("2. Work Done (Constant External Pressure)")
        print("3. Work Done (Reversible Expansion/Compression)")
        print("4. Sensible Heat at Constant Pressure")
        print("5. Percent Decrease in Heat")
        print("6. Exit")
        choice = input("Select an option (1-6): ")

        if choice == "1":
            # Heat of Reaction
            known_enthalpies = {}
            coefficients = {}
            reaction_heat = float(input("Enter heat of reaction (kJ): "))

            num_components = int(input("Enter number of components: "))
            for _ in range(num_components):
                component = input("Component name: ")
                coeff = float(input(f"Coefficient for {component}: "))
                enthalpy = input(f"Heat of formation for {component} (kJ/mol or 'unknown'): ")
                enthalpy = None if enthalpy.lower() == "unknown" else float(enthalpy)
                known_enthalpies[component] = enthalpy
                coefficients[component] = coeff

            unknown_component, unknown_heat = heat_of_reaction(known_enthalpies, reaction_heat, coefficients)
            print(f"Heat of formation for {unknown_component}: {unknown_heat:.2f} kJ/mol")

        elif choice == "2":
            # Work Done at Constant Pressure
            pressure = float(input("Enter external pressure (atm): "))
            v_initial = float(input("Enter initial volume (L): "))
            v_final = float(input("Enter final volume (L): "))
            work = work_done_external_pressure(pressure, v_initial, v_final)
            print(f"Work done: {work:.2f} kJ")

        elif choice == "3":
            # Reversible Work
            n_moles = float(input("Enter number of moles of gas: "))
            t_kelvin = float(input("Enter temperature (K): "))
            v_initial = float(input("Enter initial volume (L): "))
            v_final = float(input("Enter final volume (L): "))
            work = reversible_work(n_moles, t_kelvin, v_initial, v_final)
            print(f"Reversible work done: {work:.2f} kJ")

        elif choice == "4":
            # Sensible Heat at Constant Pressure
            heat_released = float(input("Enter heat released (J): "))
            internal_energy_change = float(input("Enter change in internal energy (J): "))
            enthalpy_change = sensible_heat_constant_pressure(heat_released, internal_energy_change)
            print(f"Change in enthalpy: {enthalpy_change:.2f} kJ")

        elif choice == "5":
            # Percent Decrease in Heat
            initial_heat = float(input("Enter initial heat of combustion (kJ): "))
            absorbed_heat = float(input("Enter absorbed heat (kJ): "))
            percent = percent_decrease_heat(initial_heat, absorbed_heat)
            print(f"Percent decrease in heat: {percent:.2f}%")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()
