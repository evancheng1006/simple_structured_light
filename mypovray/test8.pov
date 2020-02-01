#include "colors.inc"
#include "glass.inc"
#include "golds.inc"
#include "metals.inc"
#include "stones.inc"
#include "woods.inc"
#include "textures.inc"          

  
camera {  sky <0,0,1>  direction <-1,0,0>  right <1,0,0>  location  <0,0,100>  look_at   <0,0,0> angle 30 }


global_settings { ambient_light White }
light_source { <0,0,100>  color White*0.5 }   


background { color White }

//plane { <0, 0, 1>, 0 texture {T_Wood15} } 

                                  
         
plane { <0, 0, 1>, 0 pigment { checker color <0.5,0.5,0.5>, color <1,1,1> } }



//light_source { <0,0,10> color White spotlight radius 63.4349 falloff 63.4349 point_at <0,0,0>} 
light_source {<0.000000,0.000000,10.000000> color White spotlight radius 18.434949 falloff 18.434949 point_at <-6.666667,-6.666667,0.000000>}
light_source {<0.000000,0.000000,10.000000> color White spotlight radius 18.434949 falloff 18.434949 point_at <-6.666667,0.000000,0.000000>}
light_source {<0.000000,0.000000,10.000000> color White spotlight radius 18.434949 falloff 18.434949 point_at <-6.666667,6.666667,0.000000>}
light_source {<0.000000,0.000000,10.000000> color White spotlight radius 18.434949 falloff 18.434949 point_at <0.000000,-6.666667,0.000000>}
light_source {<0.000000,0.000000,10.000000> color White spotlight radius 18.434949 falloff 18.434949 point_at <0.000000,0.000000,0.000000>}
light_source {<0.000000,0.000000,10.000000> color White spotlight radius 18.434949 falloff 18.434949 point_at <0.000000,6.666667,0.000000>}
light_source {<0.000000,0.000000,10.000000> color White spotlight radius 18.434949 falloff 18.434949 point_at <6.666667,-6.666667,0.000000>}
light_source {<0.000000,0.000000,10.000000> color White spotlight radius 18.434949 falloff 18.434949 point_at <6.666667,0.000000,0.000000>}
light_source {<0.000000,0.000000,10.000000> color White spotlight radius 18.434949 falloff 18.434949 point_at <6.666667,6.666667,0.000000>}
