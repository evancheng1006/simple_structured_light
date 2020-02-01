#include "my_objects.inc"

#include "colors.inc"
#include "glass.inc"
#include "golds.inc"
#include "metals.inc"
#include "stones.inc"
#include "woods.inc"
#include "textures.inc"          

  
camera { location  <0,0,0>  look_at <0,0,1> sky<0,0,-1> right<1,0,0>
                matrix <1, 0, 0,
                0, 1, 0
                0, 0, -1
                0, 0, 10> angle 53.1301024 }

// x_camera_w = 2 * math.tan(53.1301024 * math.pi / 360.0)
// y_camera_w = 2 * math.tan(53.1301024 * math.pi / 360.0)				
// camera_intrinsic_matrix = [[res_w/x_camera_w, 0, (res_w+1)*0.5], [0, res_h/y_camera_w, (res_h+1)*0.5], [0, 0, 1]]


global_settings { ambient_light White }
light_source { <0,0,100>  color White*0.5 }   


background { color White }

plane { <0, 0, 1>, 0 pigment { checker color <0.5,0.5,0.5>, color <1,1,1> } }

object { projector_full_low_res
//object { projector_full_very_low_res
		// flip
        matrix <1, 0, 0,
                0, 1, 0
                0, 0, -1
                0, 0, 0>
		// translate
        matrix <1, 0, 0,
                0, 1, 0
                0, 0, 1
                0, 0, 25>
		// rotate -30 degrees along x axis
        matrix <1, 0, 0,
                0, 0.86602540378, 0.5
                0, -0.5, 0.86602540378
                0, 0, 0>
		// rotate 45 degrees along y axis
        matrix <0.707106781, 0, -0.707106781,
                0, 1, 0
                0.707106781, 0, 0.707106781,
                0, 0, 0>
		}
