import bpy
import bmesh
import webbrowser
from mathutils import Quaternion
from mathutils import Vector
from bpy.props import (StringProperty, PointerProperty, EnumProperty, BoolProperty)
from bpy.types import (Panel, Operator, AddonPreferences, PropertyGroup)

class SimsVismeaSoundsPanelnew(bpy.types.Panel):
    bl_label = "Sims Vismea (new)"
    bl_idname = "OBJECT_PT_bone_transformNew"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'SimsVRC'
    bl_order = 1
    #@classmethod
    #def poll(cls, context):
    #    preferences = bpy.context.preferences.addons['BlenderVRchatVismeaCreater'].preferences
    #    return preferences.Boners_enum1 == "OPTION1"
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        sims_vismea_props = context.scene.sims_vismea_props

        layout.label(text="Select jaw bone:")
        layout.prop_search(sims_vismea_props, "selected_jaw_bone", bpy.data.objects[context.object.name].pose, "bones", text="")

        row = layout.row()
        row.label(text="Lmouth")
        row.label(text="Rmouth")

        row = layout.row()
        row.prop_search(sims_vismea_props, "selected_lmouth_bone", bpy.data.objects[context.object.name].pose, "bones", text="")
        row.prop_search(sims_vismea_props, "selected_rmouth_bone", bpy.data.objects[context.object.name].pose, "bones", text="")

        row = layout.row()
        row.operator("object.bone_transform")
        row.operator("object.bone_transform2")
        row.operator("object.bone_transform3")

        row = layout.row()
        row.operator("pose.clear_operator", icon='OUTLINER_OB_ARMATURE')

        row = layout.row()
        row.label(text="Eyes")

        row = layout.row()
        row.prop_search(sims_vismea_props, "SL_UpLid", bpy.data.objects[context.object.name].pose, "bones", text="")
        row.prop_search(sims_vismea_props, "SR_LoLid", bpy.data.objects[context.object.name].pose, "bones", text="")

        row = layout.row()
        row.prop_search(sims_vismea_props, "SL_UpLid", bpy.data.objects[context.object.name].pose, "bones", text="")
        row.prop_search(sims_vismea_props, "SR_LoLid", bpy.data.objects[context.object.name].pose, "bones", text="")

        row = layout.row()
        row.operator("object.rotate_l_uplid")
        row.operator("object.rotate_l_lolid")

        row = layout.row()
        row.operator("object.rotatebotheye")

#create new panels for the sliders, then split them for each button??

class SVSsPNAA(bpy.types.Panel):
    bl_label = "AA sound values"
    bl_idname = "OBJECT_PT_bone_transformNewAA"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'SimsVRC'
    bl_order = 1
    #@classmethod
    #def poll(cls, context):
    #    preferences = bpy.context.preferences.addons['BlenderVRchatVismeaCreater'].preferences
    #    return preferences.Boners_enum1 == "OPTION1"
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        sims_vismea_props = context.scene.sims_vismea_props


        row = layout.row()
        row.label(text="Jaw Rotation:")
        row.prop(sims_vismea_props, "jaw_rotation_AA", slider=True)

        row = layout.row()
        row.label(text="Lmouth X Location:")
        row.prop(sims_vismea_props, "lmouth_location_x_AA", slider=True)

        row = layout.row()
        row.label(text="Rmouth X Location:")
        row.prop(sims_vismea_props, "rmouth_location_x_AA", slider=True)

        if is_pose_mode(context):
            layout.label(text="Pose mode")
        elif is_edit_mode(context):
            layout.label(text="Edit mode")
        else:
            layout.label(text="Other mode")

class SVSsPNEYES(bpy.types.Panel):
    bl_label = "Eye Values"
    bl_idname = "OBJECT_PT_bone_transformNeEYEs"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'SimsVRC'
    bl_order = 1
    #@classmethod
    #def poll(cls, context):
    #    preferences = bpy.context.preferences.addons['BlenderVRchatVismeaCreater'].preferences
    #    return preferences.Boners_enum1 == "OPTION1"
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        sims_vismea_props = context.scene.sims_vismea_props

        #if is_object_mode(context):
        #    layout = self.layout
        #    layout.label(text="You need to be in pose mode", icon='ERROR')
        #else:
        row = layout.row()
        row.label(text="Left up")
        row.prop(sims_vismea_props, "L_UpLidrotate", slider=True)

        row = layout.row()
        row.label(text="Left down")
        row.prop(sims_vismea_props, "L_LoLidrotate", slider=True)

        row = layout.row()
        row.label(text="right up")
        row.prop(sims_vismea_props, "R_UpLidrotate", slider=True)

        row = layout.row()
        row.label(text="right down")
        row.prop(sims_vismea_props, "R_LoLidrotate", slider=True)

        if is_pose_mode(context):
            layout.label(text="Pose mode")
        elif is_edit_mode(context):
            layout.label(text="Edit mode")
        else:
            layout.label(text="Other mode")


class SVSsPNOH(bpy.types.Panel):
    bl_label = "OH sound values"
    bl_idname = "OBJECT_PT_bone_transformNewOH"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'SimsVRC'
    bl_order = 1
    #@classmethod
    #def poll(cls, context):
    #    preferences = bpy.context.preferences.addons['BlenderVRchatVismeaCreater'].preferences
    #    return preferences.Boners_enum1 == "OPTION1"
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        sims_vismea_props = context.scene.sims_vismea_props

        row = layout.row()
        row.label(text="Jaw Rotation:")
        row.prop(sims_vismea_props, "jaw_rotation_OH", slider=True)

        row = layout.row()
        row.label(text="Lmouth X Location:")
        row.prop(sims_vismea_props, "lmouth_location_x_OH", slider=True)

        row = layout.row()
        row.label(text="Rmouth X Location:")
        row.prop(sims_vismea_props, "rmouth_location_x_OH", slider=True)

        if is_pose_mode(context):
            layout.label(text="Pose mode")
        elif is_edit_mode(context):
            layout.label(text="Edit mode")
        else:
            layout.label(text="Other mode")

class SVSsPNCH(bpy.types.Panel):
    bl_label = "CH sound values"
    bl_idname = "OBJECT_PT_bone_transformNewCH"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'SimsVRC'
    bl_order = 1
    #@classmethod
    #def poll(cls, context):
    #    preferences = bpy.context.preferences.addons['BlenderVRchatVismeaCreater'].preferences
    #    return preferences.Boners_enum1 == "OPTION1"
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        sims_vismea_props = context.scene.sims_vismea_props

        row = layout.row()
        row.label(text="Jaw Rotation:")
        row.prop(sims_vismea_props, "jaw_rotation_CH", slider=True)

        row = layout.row()
        row.label(text="Lmouth X Location:")
        row.prop(sims_vismea_props, "lmouth_location_x_CH", slider=True)

        row = layout.row()
        row.label(text="Rmouth X Location:")
        row.prop(sims_vismea_props, "rmouth_location_x_CH", slider=True)

        if is_pose_mode(context):
            layout.label(text="Pose mode")
        elif is_edit_mode(context):
            layout.label(text="Edit mode")
        else:
            layout.label(text="Other mode")


def is_pose_mode(context):
    return context.mode == 'POSE'

def is_object_mode(context):
    return context.mode == 'OBJECT'

def is_edit_mode(context):
    return context.mode == 'EDIT'

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

def rotate_bone(bone, axis, angle):
    bone.rotation_quaternion.rotate(Quaternion(axis, angle))

def move_bone(bone, axis, value):
    if axis == 'x':
        bone.location.x = value
    elif axis == 'y':
        bone.location.y = value
    elif axis == 'z':
        bone.location.z = value

class BoneTransformAAOperatorold(bpy.types.Operator):
    """Moves the character mouth to mimic the sound of AA"""
    bl_idname = "object.bone_transform"
    bl_label = "AA"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        sims_vismea_props = context.scene.sims_vismea_props
        armature = bpy.data.objects.get("Armature")
        if not armature:
            return {'CANCELLED'}

        selected_jaw_bonee = armature.pose.bones.get(sims_vismea_props.selected_jaw_bone)
        selected_lmouth_bonee = armature.pose.bones.get(sims_vismea_props.selected_lmouth_bone)
        selected_rmouth_bonee = armature.pose.bones.get(sims_vismea_props.selected_rmouth_bone)

        if not selected_jaw_bonee or not selected_lmouth_bonee or not selected_rmouth_bonee:
            self.report({'ERROR'}, "Selected bones not found")
            return {'CANCELLED'}

        rotate_bone(selected_jaw_bonee, (1, 0, 0), sims_vismea_props.jaw_rotation_AA)
        move_bone(selected_lmouth_bonee, 'x', sims_vismea_props.lmouth_location_x_AA)
        move_bone(selected_rmouth_bonee, 'x', sims_vismea_props.rmouth_location_x_AA)

        return {'FINISHED'}


class SimsVismeaPropertyGroup(bpy.types.PropertyGroup):
    selected_jaw_bone: bpy.props.StringProperty(
        name="Selected Jaw Bone",
        description="Name of the selected jaw bone",
        default="Jaw"
    )
    selected_lmouth_bone: bpy.props.StringProperty(
        name="Selected Left Mouth Bone",
        description="Name of the selected left mouth bone",
        default="L_Mouth"
    )
    selected_rmouth_bone: bpy.props.StringProperty(
        name="Selected Right Mouth Bone",
        description="Name of the selected right mouth bone",
        default="R_Mouth"
    )
    jaw_rotation_AA: bpy.props.FloatProperty(
        name="Jaw Rotation",
        description="Rotation of the jaw bone",
        default=0.09,
        min=0.0,
        max=1.0
    )
    lmouth_location_x_AA: bpy.props.FloatProperty(
        name="Left Mouth X Location",
        description="X location of the left mouth bone",
        default=-0.01
    )
    rmouth_location_x_AA: bpy.props.FloatProperty(
        name="Right Mouth X Location",
        description="X location of the right mouth bone",
        default=0.01
    )
    jaw_rotation_CH: bpy.props.FloatProperty(
        name="Jaw Rotation",
        description="Rotation of the jaw bone",
        default=0.3,
        min=0.0,
        max=1.0
    )
    lmouth_location_x_CH: bpy.props.FloatProperty(
        name="Left Mouth X Location",
        description="X location of the left mouth bone",
        default=-0.015
    )
    rmouth_location_x_CH: bpy.props.FloatProperty(
        name="Right Mouth X Location",
        description="X location of the right mouth bone",
        default=0.015
    )
    jaw_rotation_OH: bpy.props.FloatProperty(
        name="Jaw Rotation",
        description="Rotation of the jaw bone",
        default=0.2,
        min=0.0,
        max=1.0
    )
    lmouth_location_x_OH: bpy.props.FloatProperty(
        name="Left Mouth X Location",
        description="X location of the left mouth bone",
        default=-0.015
    )
    rmouth_location_x_OH: bpy.props.FloatProperty(
        name="Right Mouth X Location",
        description="X location of the right mouth bone",
        default=0.015
    )#Left eye
    SL_UpLid: bpy.props.StringProperty(
        name="Selected Jaw Bone",
        description="The upper lid",
        default="L_UpLid"
    )
    SL_LoLid: bpy.props.StringProperty(
        name="Selected Jaw Bone",
        description="The lower lid",
        default="L_LoLid"
    )
    L_UpLidrotate: bpy.props.FloatProperty(
        name="Left Mouth X Location",
        description="X location of the left mouth bone",
        default=-0.349066
    )
    L_LoLidrotate: bpy.props.FloatProperty(
        name="Right Mouth X Location",
        description="X location of the right mouth bone",
        default=0.349066
    )#Right eye
    SR_UpLid: bpy.props.StringProperty(
        name="Selected Jaw Bone",
        description="Name of the selected jaw bone",
        default="R_UpLid"
    )
    SR_LoLid: bpy.props.StringProperty(
        name="Selected Jaw Bone",
        description="Name of the selected jaw bone",
        default="R_LoLid"
    )
    R_UpLidrotate: bpy.props.FloatProperty(
        name="Left Mouth X Location",
        description="X location of the left mouth bone",
        default=-0.349066
    )
    R_LoLidrotate: bpy.props.FloatProperty(
        name="Right Mouth X Location",
        description="X location of the right mouth bone",
        default=0.349066
    )
#L_UpLid -0.349066
#L_LoLid 0.349066

class BoneTransformOHOperatorold(bpy.types.Operator):
    """Moves the characher mouth to momick the sound of OH"""
    bl_idname = "object.bone_transform2"
    bl_label = "OH"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        sims_vismea_props = context.scene.sims_vismea_props
        armature = bpy.data.objects.get("Armature")
        if not armature:
            return {'CANCELLED'}

        selected_jaw_bonee = armature.pose.bones.get(sims_vismea_props.selected_jaw_bone)
        selected_lmouth_bonee = armature.pose.bones.get(sims_vismea_props.selected_lmouth_bone)
        selected_rmouth_bonee = armature.pose.bones.get(sims_vismea_props.selected_rmouth_bone)

        if not selected_jaw_bonee or not selected_lmouth_bonee or not selected_rmouth_bonee:
            self.report({'ERROR'}, "Selected bones not found")
            return {'CANCELLED'}

        rotate_bone(selected_jaw_bonee, (1, 0, 0), sims_vismea_props.jaw_rotation_OH)
        move_bone(selected_lmouth_bonee, 'x', sims_vismea_props.lmouth_location_x_OH)
        move_bone(selected_rmouth_bonee, 'x', sims_vismea_props.rmouth_location_x_OH)

        return {'FINISHED'}

class BoneTransformCHOperatorold(bpy.types.Operator):
    """Moves the characher mouth to momick the sound of CH"""
    bl_idname = "object.bone_transform3"
    bl_label = "Ch"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        sims_vismea_props = context.scene.sims_vismea_props
        armature = bpy.data.objects.get("Armature")
        if not armature:
            return {'CANCELLED'}

        selected_jaw_bonee = armature.pose.bones.get(sims_vismea_props.selected_jaw_bone)
        selected_lmouth_bonee = armature.pose.bones.get(sims_vismea_props.selected_lmouth_bone)
        selected_rmouth_bonee = armature.pose.bones.get(sims_vismea_props.selected_rmouth_bone)

        if not selected_jaw_bonee or not selected_lmouth_bonee or not selected_rmouth_bonee:
            self.report({'ERROR'}, "Selected bones not found")
            return {'CANCELLED'}

        rotate_bone(selected_jaw_bonee, (1, 0, 0), sims_vismea_props.jaw_rotation_CH)
        move_bone(selected_lmouth_bonee, 'x', sims_vismea_props.lmouth_location_x_CH)
        move_bone(selected_rmouth_bonee, 'x', sims_vismea_props.rmouth_location_x_CH)

        return {'FINISHED'}

class PoseClearOperatorold(bpy.types.Operator):
    """Rsets the Charachter Pose to the defufalt"""
    bl_idname = "pose.clear_operator"
    bl_label = "Clear Pose"
    bl_description = "Clear pose location, rotation, and scale for all selected bones"
    @classmethod
    def poll(cls, context):
        return is_pose_mode(context)
    def execute(self, context):
        bpy.ops.pose.select_all(action='SELECT')
        bpy.ops.pose.loc_clear()
        bpy.ops.pose.scale_clear()
        bpy.ops.pose.rot_clear()
        bpy.ops.pose.select_all(action='DESELECT')
        self.report({'INFO'}, "Pose Cleared")
        return {'FINISHED'}
#L_UpLid -0.349066
#L_LoLid 0.349066
class RotateLUpLidOperatorold(bpy.types.Operator):
    bl_idname = "object.rotate_l_uplid"
    bl_label = "Close Left"
    bl_options = {'REGISTER', 'UNDO'}
    @classmethod
    def poll(cls, context):
        return is_pose_mode(context)
    def execute(self, context):
        sims_vismea_props = context.scene.sims_vismea_props
        armature = bpy.data.objects.get("Armature")
        if not armature:
            return {'CANCELLED'}

        L_UpLide = armature.pose.bones.get(sims_vismea_props.SL_UpLid)
        L_LoLide = armature.pose.bones.get(sims_vismea_props.SL_LoLid)

        if not L_UpLide or not L_LoLide:
            self.report({'ERROR'}, "Selected bones not found")
            return {'CANCELLED'}

        rotate_bone(L_UpLide, (1, 0, 0), sims_vismea_props.L_UpLidrotate)
        rotate_bone(L_LoLide, (1, 0, 0), sims_vismea_props.L_LoLidrotate)
        return {'FINISHED'}

class RotateLLoLidOperatorold(bpy.types.Operator):
    bl_idname = "object.rotate_l_lolid"
    bl_label = "Close Right"
    bl_options = {'REGISTER', 'UNDO'}
    @classmethod
    def poll(cls, context):
        return is_pose_mode(context)
    def execute(self, context):
        sims_vismea_props = context.scene.sims_vismea_props
        armature = bpy.data.objects.get("Armature")
        if not armature:
            return {'CANCELLED'}

        R_UpLide = armature.pose.bones.get(sims_vismea_props.SR_UpLid)
        R_LoLide = armature.pose.bones.get(sims_vismea_props.SR_LoLid)

        if not R_UpLide or not R_LoLide:
            self.report({'ERROR'}, "Selected bones not found")
            return {'CANCELLED'}

        rotate_bone(R_UpLide, (1, 0, 0), sims_vismea_props.R_UpLidrotate)
        rotate_bone(R_LoLide, (1, 0, 0), sims_vismea_props.R_LoLidrotate)
        return {'FINISHED'}

class RotateBothEOperatorold(bpy.types.Operator):
    bl_idname = "object.rotatebotheye"
    bl_label = "Close Both Eyes"
    bl_options = {'REGISTER', 'UNDO'}
    @classmethod
    def poll(cls, context):
        return is_pose_mode(context)
    def execute(self, context):
        sims_vismea_props = context.scene.sims_vismea_props
        armature = bpy.data.objects.get("Armature")
        if not armature:
            return {'CANCELLED'}

        R_UpLide = armature.pose.bones.get(sims_vismea_props.SR_UpLid)
        R_LoLide = armature.pose.bones.get(sims_vismea_props.SR_LoLid)
        L_UpLide = armature.pose.bones.get(sims_vismea_props.SL_UpLid)
        L_LoLide = armature.pose.bones.get(sims_vismea_props.SL_LoLid)

        if not R_UpLide or not R_LoLide or not L_UpLide or not L_LoLide:
            self.report({'ERROR'}, "Selected bones not found")
            return {'CANCELLED'}

        rotate_bone(R_UpLide, (1, 0, 0), sims_vismea_props.R_UpLidrotate)
        rotate_bone(R_LoLide, (1, 0, 0), sims_vismea_props.R_LoLidrotate)
        rotate_bone(L_UpLide, (1, 0, 0), sims_vismea_props.L_UpLidrotate)
        rotate_bone(L_LoLide, (1, 0, 0), sims_vismea_props.L_LoLidrotate)
        return {'FINISHED'}

def menu_funcold(self, context):
    self.layout.operator(BoneTransformAAOperatorold.bl_idname)

classes = (
    SimsVismeaSoundsPanelnew,
    SVSsPNAA,
    SVSsPNOH,
    SVSsPNCH,
    SVSsPNEYES,
    Objectmodeinold,
    ObjectmodeinoldSecoundold,
    Editmodeinold,
    Posemodeinold,
    BoneTransformAAOperatorold,
    BoneTransformOHOperatorold,
    BoneTransformCHOperatorold,
    PoseClearOperatorold,
    RotateLUpLidOperatorold,
    RotateLLoLidOperatorold,
    RotateBothEOperatorold,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.VIEW3D_MT_object.append(menu_funcold)
    bpy.utils.register_class(SimsVismeaPropertyGroup)
    bpy.types.Scene.sims_vismea_props = bpy.props.PointerProperty(type=SimsVismeaPropertyGroup)
    bpy.types.Scene.selected_jaw_bonee = bpy.props.StringProperty()
    bpy.types.Scene.L_UpLide = bpy.props.StringProperty()
    bpy.types.Scene.L_LoLide = bpy.props.StringProperty()
    bpy.types.Scene.R_UpLide = bpy.props.StringProperty()
    bpy.types.Scene.R_LoLide = bpy.props.StringProperty()


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    bpy.types.VIEW3D_MT_object.remove(menu_funcold)
    bpy.utils.register_class(SimsVismeaPropertyGroup)
    bpy.types.Scene.sims_vismea_props = bpy.props.PointerProperty(type=SimsVismeaPropertyGroup)
    del bpy.types.Scene.selected_jaw_bonee
    del bpy.types.Scene.L_UpLide
    del bpy.types.Scene.L_LoLide
    del bpy.types.Scene.R_UpLide
    del bpy.types.Scene.R_LoLide

if __name__ == "__main__":
    register()
