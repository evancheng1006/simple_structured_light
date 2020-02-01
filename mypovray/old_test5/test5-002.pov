#include "colors.inc"
#include "glass.inc"
#include "golds.inc"
#include "metals.inc"
#include "stones.inc"
#include "woods.inc"
#include "textures.inc"          

  
camera {  sky <0,0,1>  direction <-1,0,0>  right <1,0,0>  location  <90,20,150>  look_at   <0,0,0>  angle 15 }


global_settings { ambient_light White }
light_source { <0,0,100>  color White*0.5 }      
light_source { <-400,-715,1005>  color <0.6,0.2,0.7> } 
light_source { <2134,801,925>  color <0.3,0.9,0.1> }


background { color White }

plane { <0, 0, 1>, 0 texture {T_Wood15} } 

                                  
                     
                     
sphere { <1.5, 5, 2>, 4  texture {T_Chrome_2A} }
box { <-5,-5,0> <5,5,10> texture{T_Grnt2}  rotate <0, 0, -25>}
box { <-2.5,-2.5,9> <3.5,3.5,13> texture{T_Grnt2}  rotate <0, 0, 5>} 




#for (CntX, 0, 199, 1)   
  #for (CntY, 0, 199, 1)
       #if (CntY/40 - int(CntY/40) < 0.5) 
         light_source { <50,0,150> color White spotlight radius 0.028 falloff 0.028 point_at <-9.95+CntX*0.1,-9.95+CntY*0.1,0> }
       #end
  #end
#end







