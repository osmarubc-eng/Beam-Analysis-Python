from src.beam import Beam 
from src.plotter import BeamPlotter


def main():
    
    beam = Beam(length=8) 

    beam.add_point_load(force=2500, position=3)   

    beam.add_point_load(force=1200, position=6)

    beam.add_point_load(force=800, position=7) 

    print(f"hay {len(beam.loads):.2f} cargas")

    beam.calculate_reactions()

    print(f"Longitud: {beam.length:.2f} m")
    

    

    print("\nCargas:")

    for i, load in enumerate(beam.loads, start=1):

        print(
        f"Carga {i}: "
        f"{load.force:.2f} kgf "
        f"en x = {load.position:.2f} m"
        )


    print(f"\nReacción A = {beam.reaction_A:.2f} kgf")
    print(f"Reacción B = {beam.reaction_B:.2f} kgf")

    print(f"\nV(2.0) = {beam.shear(2.0):.2f} kgf")
    print(f"V(4.0) = {beam.shear(4.0):.2f} kgf")
    print(f"V(6.5) = {beam.shear(6.5):.2f} kgf")
    print(f"V(7.5) = {beam.shear(7.5):.2f} kgf")





    BeamPlotter.plot_shear(beam)
    
   

    



    print()
    print("Moments")

    for x in [0, 2, 3, 4, 6, 7, 8]:
        print(f"M({x}) = {beam.moment(x):.2f} kgf·m")

        


    

if __name__ == "__main__":
    main()


