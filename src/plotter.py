import matplotlib.pyplot as plt


class BeamPlotter:

    @staticmethod
    def _draw_beam(ax, beam):

        ax.hlines(
            y=0,
            xmin=0,
            xmax=beam.length,
            linewidth=4
     
         )
        
    @staticmethod
    def _draw_supports(ax, beam):

        ax.scatter(
            [0, beam.length],
            [0, 0],
            marker="^",
            s=180
        )


    @staticmethod
    def _format_structure_axes(ax):

        ax.set_ylim(-1.5, 1.0)

        ax.set_yticks([])

        ax.set_xticks([])

        for spine in ax.spines.values():
            spine.set_visible(False)


    @staticmethod
    def _draw_point_loads(ax, beam):

        for load in beam.loads:

            ax.annotate(
                "",
                xy=(load.position, 0),
                xytext=(load.position, 0.6),
                arrowprops=dict(
                    arrowstyle="->",
                    lw=2
                )
            )

            ax.text(
                load.position,
                0.65,
                f"{load.force:.0f}",
                ha="center",
                fontsize=9
            )


    @staticmethod
    def _draw_reactions(ax, beam):

        ax.annotate(
            "",
            xy=(0, 0),
            xytext=(0, -0.6),
            arrowprops=dict(
                arrowstyle="->",
                lw=2
            )
        )

        ax.text(
             0,
            -0.80,
            f"{beam.reaction_A:.1f}",
            ha="center"
        )

        ax.annotate(
            "",
            xy=(beam.length, 0),
            xytext=(beam.length, -0.6),
            arrowprops=dict(
                arrowstyle="->",
                lw=2
            )
        )

        ax.text(
            beam.length,
            -0.80,
            f"{beam.reaction_B:.1f}",
            ha="center"
        )





    @staticmethod
    def plot_shear(beam):

        x_values, V_values = beam.shear_diagram()

        fig, (ax_beam, ax_shear) = plt.subplots(
            2,
            1,
            figsize=(12,6),
            sharex=True,
            gridspec_kw={"height_ratios":[1,3]}
        )
        
        BeamPlotter._draw_beam(ax_beam, beam)

        BeamPlotter._draw_supports(ax_beam, beam)

        BeamPlotter._draw_point_loads(ax_beam, beam)

        BeamPlotter._draw_reactions(ax_beam, beam)

        BeamPlotter._format_structure_axes(ax_beam)

        


        ax_shear.step(x_values, V_values, where="post", linewidth=2)

        ax_shear.fill_between(
            x_values,
            V_values,
            0,
            step="post",
            alpha=0.3
        )
        
        ax_shear.axhline(0)

        ax_shear.set_title("Shear Force Diagram")

        ax_shear.set_xlabel("Position (m)")

        ax_shear.set_ylabel("Shear (kgf)")

        ax_shear.grid(True)
        
        ax_shear.invert_yaxis()

        plt.tight_layout()
        plt.show()

        