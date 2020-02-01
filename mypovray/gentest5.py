

# Filename: gentest5.py

pov_basename = 'test5'

projectors = [
'projector_full_256_256',
'projector_256_256_mod_y_256_lt_128',
'projector_256_256_mod_y_128_lt_64',
'projector_256_256_mod_y_64_lt_32',
'projector_256_256_mod_y_32_lt_16',
'projector_256_256_mod_y_16_lt_8',
'projector_256_256_mod_y_8_lt_4',
'projector_256_256_mod_y_4_lt_2',
'projector_256_256_mod_y_2_lt_1',
'projector_256_256_mod_x_256_lt_128',
'projector_256_256_mod_x_128_lt_64',
'projector_256_256_mod_x_64_lt_32',
'projector_256_256_mod_x_32_lt_16',
'projector_256_256_mod_x_16_lt_8',
'projector_256_256_mod_x_8_lt_4',
'projector_256_256_mod_x_4_lt_2',
'projector_256_256_mod_x_2_lt_1'
]

pre = '''
#include "my_objects.inc"

#include "colors.inc"
#include "glass.inc"
#include "golds.inc"
#include "metals.inc"
#include "stones.inc"
#include "woods.inc"
#include "textures.inc"
#include "shapes.inc"      
#include "shapes3.inc"    

  
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

object {
'''
post = '''
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



//----------------------------------------------------------------------------
#declare small_tube = object{ Rounded_Tube( 0.50, // tube radius outside
                      0.49, // tube inner radius 
                      0.00, // border radius 
                      3.00, // tube high
                      1, // 0 = union, 1 = merge for transparent materials 
                    ) //------------------------------------------------------  
        texture{ T_Stone3 } // end texture
        scale <1,1,1> 

      } // end of object -----------------------------------------------------
//----------------------------------------------------------------------------

#declare fixed_tube = object { small_tube translate<0,-2,0> rotate<-28,0,0> translate<0,0,1> }

object { fixed_tube rotate<0,0,10> }
'''

for projector in projectors:
    fn = "%s_%s.pov" % (pov_basename, projector)
    print(fn)
    pov_data = "%s\n%s\n%s\n" % (pre, projector, post)
    #print(pov_data)
    
    with open(fn, 'w') as f:
        f.write(pov_data)
        
 
 