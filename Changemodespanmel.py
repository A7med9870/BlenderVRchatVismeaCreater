import bpy
import bmesh
import webbrowser
from mathutils import Quaternion
from mathutils import Vector
from bpy.props import (StringProperty, PointerProperty, EnumProperty, BoolProperty)
from bpy.types import (Panel, Operator, AddonPreferences, PropertyGroup)

class SimsVismeaSoundsPanelcms(bpy.types.Panel):
    bl_label = "Change mode"
    bl_idname = "OBJECT_PT_bone_transformcms"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'SimsVRC'
    bl_order = 1
    @classmethod
    def poll(cls, context):
        preferences = bpy.context.preferences.addons['BlenderVRchatVismeaCreater'].preferences
        return preferences.Boners_enum1 == "OPTION1"
    def draw(self, context):
        layout = self.layout
        scene = context.scene

        row = layout.row()
        if is_object_mode(context):
            row = layout.row()
            row.operator("object.apply_posemode", icon='POSE_HLT')
            row.operator("object.apply_editmode", icon='EDITMODE_HLT')
        elif is_pose_mode(context):
            row = layout.row()
            row.operator("object.apply_objectmode", icon='OBJECT_DATAMODE')
            row.operator("object.apply_editmode", icon='EDITMODE_HLT')
        else:
            row = layout.row()
            row.operator("object.apply_posemode", icon='POSE_HLT')
            row.operator("object.apply_objectmodesec")

def is_pose_mode(context):
    return context.mode == 'POSE'

def is_object_mode(context):
    return context.mode == 'OBJECT'

def is_edit_mode(context):
    return context.mode == 'EDIT'

def menu_funcseccsec(self, context):
    self.layout.operator(BoneTransformAAOperatorold.bl_idname)

class Objectmodeinold(bpy.types.Operator):
    """Enter Object Mode"""
    bl_idname = "object.apply_objectmode"
    bl_label = "Object Mode"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}

class ObjectmodeinoldSecoundold(bpy.types.Operator):
    """Enter Object Mode"""
    bl_idname = "object.apply_objectmodesec"
    bl_label = "Object Mode"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}

class Editmodeinold(bpy.types.Operator):
    """Enter Editing Mode"""
    bl_idname = "object.apply_editmode"
    bl_label = "Edit Mode"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}

class Posemodeinold(bpy.types.Operator):
    """Enter Pose Mode"""
    bl_idname = "object.apply_posemode"
    bl_label = "Pose Mode"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        bpy.ops.object.posemode_toggle()
        return {'FINISHED'}

classes = (
    SimsVismeaSoundsPanelcms,
    Objectmodeinold,
    ObjectmodeinoldSecoundold,
    Editmodeinold,
    Posemodeinold,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.VIEW3D_MT_object.append(menu_funcseccsec)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    bpy.types.VIEW3D_MT_object.remove(menu_funcseccsec)

if __name__ == "__main__":
    register()
