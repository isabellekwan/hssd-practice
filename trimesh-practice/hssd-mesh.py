import trimesh

def load_and_visualize_mesh(mesh_file):
    # Load the mesh file
    mesh = trimesh.load(mesh_file)
    
    # Visualize the mesh
    mesh.show()

if __name__ == "__main__":
    # Replace 'path/to/your/mesh.obj' with the actual path to your mesh file
    mesh_file = '/localhome/itk1/Habitat-Code/hssd-downloads/versioned_data/habitat_example_objects_0.2/cheezit.glb'
    
    # Call the function to load and visualize the mesh
    load_and_visualize_mesh(mesh_file)