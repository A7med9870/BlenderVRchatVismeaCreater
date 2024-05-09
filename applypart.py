import bpy
import bmesh
import webbrowser
from mathutils import Vector
from bpy.props import (StringProperty, PointerProperty, EnumProperty, BoolProperty)
from bpy.types import (Panel, Operator, AddonPreferences, PropertyGroup)

def is_pose_mode(context):
    return context.mode == 'POSE'

def is_object_mode(context):
    return context.mode == 'OBJECT'

class VRCVismeaApplyPanel(bpy.types.Panel):
    bl_label = "Applying shape keys"
    bl_idname = "OBJECT_PT_vrcvismea_apply"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'SimsVRC'
    bl_order = 2

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Apply Shapekey")

        row = layout.row()
        row.operator("object.apply_armature_shapekey")
        row.operator("object.apply_armature_shapekeyoh")
        row.operator("object.apply_armature_shapekeych")

        row = layout.row()
        row.operator("object.apply_armatureel")
        row.operator("object.apply_armatureer")

        row = layout.row()
        row.operator("object.apply_armatureb")

        if is_object_mode(context):
            row = layout.row()
            row.label(text="1")
        elif is_pose_mode(context):
            row = layout.row()
            row.label(text="2")
            layout.label(text="You need to be on Object", icon='ERROR')
        else:
            row = layout.row()
            row.label(text="3")

class AAASKOAA(bpy.types.Operator):
    """Moves the character mouth to mimic the sound of AA"""
    bl_idname = "object.apply_armature_shapekey"
    bl_label = "AA_s"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return is_object_mode(context)
    def execute(self, context):
        armature = bpy.data.objects.get("Armature")
        body = bpy.data.objects.get("Body")
        current_object = context.object

        if current_object.type == 'MESH':
            bpy.ops.object.modifier_apply_as_shapekey(keep_modifier=True, modifier="Armature")
            # Find the newly created shape key
            shape_keys = current_object.data.shape_keys
            if shape_keys:
                shape_key = shape_keys.key_blocks[-1]
                shape_key.name = "AA_sound"
                self.report({'INFO'}, "Shape key (AA_sound) has been created, you can see it under Data > Shape Keys")
                return {'FINISHED'}
        elif current_object == armature:
            self.report({'ERROR'}, "Please select the mesh; you have selected the armature now.")
        elif current_object == body:
            self.report({'ERROR'}, "Please rename the mesh too (Body)")

        return {'CANCELLED'}

class AAASKOOH(bpy.types.Operator):
    bl_idname = "object.apply_armature_shapekeyoh"
    bl_label = "OH_s"
    bl_options = {'REGISTER', 'UNDO'}
    @classmethod
    def poll(cls, context):
        return is_object_mode(context)
    def execute(self, context):
        armature = bpy.data.objects.get("Armature")
        if not armature:
            self.report({'ERROR'}, "Please select the character mesh")
            return {'CANCELLED'}
        bpy.ops.object.modifier_apply_as_shapekey(keep_modifier=True, modifier="Armature")
        # Find the newly created shape key
        shape_key = context.active_object.data.shape_keys.key_blocks[-1]
        if shape_key:
            shape_key.name = "OH_sound"
        self.report({'INFO'}, "Shape key (OH_sound) has been created, ")
        return {'FINISHED'}

class AAASKOCH(bpy.types.Operator):
    bl_idname = "object.apply_armature_shapekeych"
    bl_label = "CH_s"
    bl_options = {'REGISTER', 'UNDO'}
    @classmethod
    def poll(cls, context):
        return is_object_mode(context)
    def execute(self, context):
        armature = bpy.data.objects.get("Armature")
        if not armature:
            self.report({'ERROR'}, "Please select the character mesh")
            return {'CANCELLED'}
        bpy.ops.object.modifier_apply_as_shapekey(keep_modifier=True, modifier="Armature")
        # Find the newly created shape key
        shape_key = context.active_object.data.shape_keys.key_blocks[-1]
        if shape_key:
            shape_key.name = "CH_sound"
        self.report({'INFO'}, "Shape key (CH_sound) has been created, ")
        return {'FINISHED'}

class AAASOeyeL(bpy.types.Operator):
    bl_idname = "object.apply_armatureel"
    bl_label = "S_EYE_L"
    bl_options = {'REGISTER', 'UNDO'}
    @classmethod
    def poll(cls, context):
        return is_object_mode(context)
    def execute(self, context):
        armature = bpy.data.objects.get("Armature")
        if not armature:
            self.report({'ERROR'}, "Please select the character mesh")
            return {'CANCELLED'}
        bpy.ops.object.modifier_apply_as_shapekey(keep_modifier=True, modifier="Armature")
        # Find the newly created shape key
        shape_key = context.active_object.data.shape_keys.key_blocks[-1]
        if shape_key:
            shape_key.name = "BlinkLeft"
        return {'FINISHED'}

class AAASOeyeR(bpy.types.Operator):
    bl_idname = "object.apply_armatureer"
    bl_label = "S_EYE_R"
    bl_options = {'REGISTER', 'UNDO'}
    @classmethod
    def poll(cls, context):
        return is_object_mode(context)
    def execute(self, context):
        armature = bpy.data.objects.get("Armature")
        if not armature:
            self.report({'ERROR'}, "Please select the character mesh")
            return {'CANCELLED'}
        bpy.ops.object.modifier_apply_as_shapekey(keep_modifier=True, modifier="Armature")
        # Find the newly created shape key
        shape_key = context.active_object.data.shape_keys.key_blocks[-1]
        if shape_key:
            shape_key.name = "BlinkRight"
        return {'FINISHED'}

class AAASOeyeBoth(bpy.types.Operator):
    bl_idname = "object.apply_armatureb"
    bl_label = "Both Eyes"
    bl_options = {'REGISTER', 'UNDO'}
    @classmethod
    def poll(cls, context):
        return is_object_mode(context)
    def execute(self, context):
        armature = bpy.data.objects.get("Armature")
        if not armature:
            self.report({'ERROR'}, "Please select the character mesh")
            return {'CANCELLED'}
        bpy.ops.object.modifier_apply_as_shapekey(keep_modifier=True, modifier="Armature")
        # Find the newly created shape key
        shape_key = context.active_object.data.shape_keys.key_blocks[-1]
        if shape_key:
            shape_key.name = "BlinkBoth"
        return {'FINISHED'}

classes = (
    VRCVismeaApplyPanel,
    AAASKOAA,
    AAASKOOH,
    AAASKOCH,
    AAASOeyeL,
    AAASOeyeR,
    AAASOeyeBoth,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
