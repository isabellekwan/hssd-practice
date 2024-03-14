import open3d as o3d
import numpy as np

# Super rainbow render below:
def load_and_visualize_glb(glb_file):
    # Load the GLB file
    mesh = o3d.io.read_triangle_mesh(glb_file)
    
    # Get the number of vertices in the mesh
    num_vertices = np.asarray(mesh.vertices).shape[0]
    
    # Generate random colors for each vertex
    colors = np.random.rand(num_vertices, 3)
    
    # Assign the random colors to the mesh vertices
    mesh.vertex_colors = o3d.utility.Vector3dVector(colors)
    
    # Visualize the mesh
    o3d.visualization.draw_geometries([mesh])

# def load_and_visualize_glb(glb_file):
#     # Load the GLB file
#     mesh = o3d.io.read_triangle_mesh(glb_file)
    
#     # Get the number of vertices in the mesh
#     vertices = np.asarray(mesh.vertices)
#     num_vertices = vertices.shape[0]
    
#     # Reduce the number of colors to half the number of vertices
#     num_colors = num_vertices // 2
    
#     # Generate random colors for all vertices
#     colors = np.random.rand(num_vertices, 3)
    
#     # Assign a subset of random colors to the mesh vertices
#     random_indices = np.random.choice(num_vertices, num_colors, replace=False)
#     mesh.vertex_colors = o3d.utility.Vector3dVector(colors[random_indices])
    
#     # Visualize the mesh
#     o3d.visualization.draw_geometries([mesh])

if __name__ == "__main__":
    # Replace 'path/to/your/file.glb' with the actual path to your GLB file
    glb_file = '/localhome/itk1/Habitat-Code/hssd-downloads/versioned_data/habitat_example_objects_0.2/skillet.glb'
    
    # Call the function to load and visualize the GLB file
    load_and_visualize_glb(glb_file)