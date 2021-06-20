import bpy
import random

#number of cubes per grid
num_of_cubes = 15  #use 25grid render

#size of the cube
size_of_cube = 3

#position
x = size_of_cube/2
y = size_of_cube/2
z = size_of_cube/2

#materials
materials_list = ['Material.001','Material.002','Material.002','Material.003','Material.004']

#random z heigth
start_z = 1
end_z = 4

#variables flaoting
x_floating = 0
y_floating = 0

print("test")
#bpy.ops.mesh.primitive_cube_add(size=size_of_cube , enter_editmode=False, align='WORLD',          location=(8,8,2.5), scale=(1, 1, 1.5))

#bpy.ops.mesh.primitive_cube_add(size=size_of_cube , enter_editmode=False, align='WORLD',          location=(8,8,2.5), scale=(1, 1, 2))

#bpy.ops.mesh.primitive_cube_add(size=size_of_cube , enter_editmode=False, align='WORLD',          location=(8,8,2.5), scale=(1, 1, 3))


#This loop is for X an Y axis generation cubes
for n in range(0,num_of_cubes):
    x_floating = 0    
    x = size_of_cube/2
    for i in range(0,num_of_cubes):
        bpy.ops.mesh.primitive_cube_add(size=size_of_cube , enter_editmode=False, align='WORLD',          location=(x,y,z), scale=(1, 1, 1))
    
        
        
        #Resize in z Axis
        random_variable_z_scale = random.uniform(start_z, end_z)
        random_variable_xy_scale = random.uniform(0.1, 0.99)
        random_variable_z_scale_medium = random.uniform(0.1, 0.5)
        
        bpy.ops.transform.resize(value=(1, 1, random_variable_z_scale), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, True, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)
        
        #Materials random
        item = bpy.context.object
        item.data.materials.append(bpy.data.materials[random.choice(materials_list)])
        
        
        
        #-----------------#
        #generate medium cubes
        bpy.ops.mesh.primitive_cube_add(size=size_of_cube , enter_editmode=False, align='WORLD',          location=(x,y,((random_variable_z_scale*size_of_cube)/2)+2*z), scale=(1, 1, 1))
        bpy.ops.transform.resize(value=(random_variable_xy_scale, random_variable_xy_scale, random_variable_z_scale_medium), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, True, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)
        
        #relocation in z
        bpy.context.object.location[2] =         bpy.context.object.location[2] - ((size_of_cube/2) - ((random_variable_z_scale_medium*size_of_cube)/2))

    
        
        
        #-----------------#
        #generate floationg cubes loop
        for j in range(0,5):
        
            bpy.ops.mesh.primitive_cube_add(size=size_of_cube*random.uniform(0.05,0.15) , enter_editmode=False, align='WORLD',          location=(x_floating +random.uniform(0,size_of_cube),y_floating+random.uniform(0,size_of_cube),((random_variable_z_scale*size_of_cube)/2)+2*random.uniform(0.5,z)), scale=(1, 1, 1))
            bpy.ops.transform.resize(value=(random_variable_xy_scale, random_variable_xy_scale, random_variable_z_scale_medium), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, True, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)
            
            
            #Materials random
            item = bpy.context.object
            item.data.materials.append(bpy.data.materials[random.choice(materials_list)])
        
        

    
        
        
        
        
        x += size_of_cube
        x_floating += size_of_cube
        
    
    
    
    
    
    
    y += size_of_cube
    y_floating += size_of_cube
    




