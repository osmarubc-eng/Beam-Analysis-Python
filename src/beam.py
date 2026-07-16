from src.loads import PointLoad


class Beam:

    # ==========================================
    # Constructor
    # ==========================================

    def __init__(self, length: float):
        
        self.length = length

        self.loads = []
       

        self.reaction_A = None
        self.reaction_B = None


     # ==========================================
     # Load Management
     # ==========================================

    def add_point_load(self, force: float, position: float) -> None:

        load = PointLoad(force, position)

        self.loads.append(load)


     # ==========================================
     # Structural Analysis
     # ==========================================

    def calculate_reactions(self):

        L = self.length

        total_load = 0
        total_moment = 0

        for load in self.loads:

            total_load += load.force
            total_moment += load.force * load.position

        RB = total_moment / L
        RA = total_load - RB

        self.reaction_A = RA
        self.reaction_B = RB

    
    def shear(self, x: float) -> float:

        if x < 0 or x > self.length:
            raise ValueError("The position x is outside the beam.")
        
        V = self.reaction_A

        for load in self.loads:

            if load.position <= x:
                V -= load.force

        return V
   



    # ==========================================
    # Post-processing
    # ==========================================

    def shear_diagram(self, step: float = 0.10):

        x_values = []

        V_values = []

        return x_values, V_values

    
   

