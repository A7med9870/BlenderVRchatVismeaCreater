import bpy
import bmesh
import webbrowser
from mathutils import Quaternion
from mathutils import Vector
from bpy.props import (StringProperty, PointerProperty, EnumProperty, BoolProperty)
from bpy.types import (Panel, Operator, AddonPreferences, PropertyGroup)

class AddBlendShapeKeyOperator(bpy.types.Operator):
    bl_idname = "object.add_blend_shape_key"
    bl_label = "Add Blend Shape Key"
    
    def execute(self, context):
        # Get the active object
        obj = context.active_object
        if obj is None or obj.type != 'MESH':
            self.report({'ERROR'}, "Select a mesh object")
            return {'CANCELLED'}
        
        # Check if a basis shape key already exists
        basis_key = obj.data.shape_keys
        if basis_key is None:
            # Create a basis shape key if it doesn't exist
            basis_key = obj.shape_key_add(name="Basis", from_mix=False)
        else:
            basis_key = basis_key.key_blocks["Basis"]
        
        # Add a new shape key and set it as the active key
        new_key = obj.shape_key_add(name="Key", from_mix=False)
        obj.active_shape_key_index = len(obj.data.shape_keys.key_blocks) - 1
        
        # Rename the last created shape key to "AA_Shapekey"
        new_key.name = "AA_Shapekey"
        self.report({'INFO'}, "Added a shape key")
        
        return {'FINISHED'}

class MyPanel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_my_panel"
    bl_label = "My Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'

    def draw(self, context):
        layout = self.layout
        
        # Get all mesh objects in the scene
        meshes = [obj for obj in bpy.context.scene.objects if obj.type == 'MESH']
        
        # Create a drop-down select box for selecting the mesh
        layout.label(text="Select Mesh:")
        layout.prop_search(context.scene, "selected_mesh", bpy.data, "objects", text="")
        
        # Add a button to add blend shape key
        layout.operator("object.add_blend_shape_key", text="Add Blend Shape Key")

def register():
    bpy.types.Scene.selected_mesh = bpy.props.StringProperty()
    bpy.utils.register_class(AddBlendShapeKeyOperator)
    bpy.utils.register_class(MyPanel)

def unregister():
    del bpy.types.Scene.selected_mesh
    bpy.utils.unregister_class(AddBlendShapeKeyOperator)
    bpy.utils.unregister_class(MyPanel)

if __name__ == "__main__":
    register()
