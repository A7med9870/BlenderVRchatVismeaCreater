import bpy
import bmesh
import webbrowser
from mathutils import Vector
from bpy.props import (StringProperty, PointerProperty, EnumProperty, BoolProperty)
from bpy.types import (Panel, Operator, AddonPreferences, PropertyGroup)

class RemoveShapeKey(Operator):
    bl_idname = "object.remove_shape_key"
    bl_label = "Remove Shape Key"
    shape_key_index: bpy.props.IntProperty()

    def execute(self, context):
        obj = context.object
        mesh = obj.data
        mesh.shape_keys.key_blocks[self.shape_key_index].value = 0.0
        bpy.ops.object.shape_key_remove(all=False)
        return {'FINISHED'}

class ShapeKeysPanel(bpy.types.Panel):
    bl_label = "Shape Keys"
    bl_idname = "OBJECT_PT_shape_keys"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'SKs'
    bl_order = 3
    
    @classmethod
    def poll(cls, context):
        return context.object is not None and context.object.type == 'MESH'

    @classmethod
    def poll(cls, context):
        preferences = context.preferences.addons['BlenderVRchatVismeaCreater'].preferences
        return preferences.show_shapekeylist_panel

    def draw(self, context):
        layout = self.layout
        obj = context.object
        mesh = obj.data

        row = layout.row()
        row.label(text="Current Shape Key:")

        if obj.active_shape_key_index >= 0:
            row = layout.row()
            row.label(text=mesh.shape_keys.key_blocks[obj.active_shape_key_index].name)

        row = layout.row()
        row.label(text="All Shape Keys:")

        for i, shape_key in enumerate(mesh.shape_keys.key_blocks):
            row = layout.row()
            row.label(text=f"{i}: {shape_key.name}")
            row.prop(shape_key, "value", text="")
            row.operator("object.remove_shape_key", text="x").shape_key_index = i

def register():
    bpy.utils.register_class(RemoveShapeKey)
    bpy.types.ShapeKey.value = bpy.props.FloatProperty(default=0.0)
    bpy.utils.register_class(ShapeKeysPanel)

def unregister():
    del bpy.types.ShapeKey.value
    bpy.utils.unregister_class(ShapeKeysPanel)

if __name__ == "__main__":
    register()
