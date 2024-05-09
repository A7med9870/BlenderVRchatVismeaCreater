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
    @classmethod
    def poll(cls, context):
        preferences = bpy.context.preferences.addons['VRCVismeaBones'].preferences
        return preferences.Boners_enum1 == "OPTION1"
    def draw(self, context):
        layout = self.layout

        obj = context.object
        if obj and obj.type == 'ARMATURE' and obj.mode == 'POSE':
            # Create a dropdown menu with all bones
            layout.prop_search(context.active_pose_bone, "name", context.active_object.pose, "bones", text="Jaw Bone")

        # rest

        row = layout.row()
        row.operator("object.bone_transform")
        row.operator("object.bone_transform2")
        row.operator("object.bone_transform3")

        row = layout.row()
        row.label(text="Eyes")

        row = layout.row()
        row.operator("object.rotate_l_uplid")
        row.operator("object.rotate_l_lolid")

        row = layout.row()
        row.operator("object.rotatebotheye")
        if is_object_mode(context):
            layout = self.layout
            layout.label(text="You need to be on pose", icon='ERROR')

        row = layout.row()
        row.label(text="")
        if is_object_mode(context):
            layout = self.layout
            layout.label(text="if object statement")
            row = layout.row()
            row.operator("object.apply_posemode", icon='POSE_HLT')
            row.operator("object.apply_editmode", icon='EDITMODE_HLT')
        elif is_pose_mode(context):
            layout = self.layout
            layout.label(text="elife pose state")
            row = layout.row()
            row.operator("object.apply_objectmode", icon='OBJECT_DATAMODE')
            row.operator("object.apply_editmode", icon='EDITMODE_HLT')
        else:
            layout = self.layout
            layout.label(text="Else statement")
            row = layout.row()
            row.operator("object.apply_posemode", icon='POSE_HLT')
            row.operator("object.apply_objectmodesec")

        row = layout.row()
        row.operator("pose.clear_operator", icon='OUTLINER_OB_ARMATURE')



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

class BoneTransformAAOperatorold(bpy.types.Operator):
    """Moves the character mouth to mimic the sound of AA"""
    bl_idname = "object.bone_transform"
    bl_label = "AA"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Set the name of the active pose bone
        bpy.context.active_pose_bone.name = "Bone"

        # Get the armature object
        armature = bpy.data.objects.get("Armature")
        if not armature:
            return {'CANCELLED'}

        sims_vismea_props = context.scene.sims_vismea_props
        selected_bone_name = sims_vismea_props.selected_bone_name

        # Get the selected bone object
        selected_bone = armature.pose.bones.get(selected_bone_name)
        if not selected_bone:
            self.report({'ERROR'}, "Selected bone not found")
            return {'CANCELLED'}

        # Rotate the selected bone (Jaw)
        if selected_bone_name == "Jaw":
            selected_bone.rotation_quaternion.rotate(Quaternion((1, 0, 0), 0.122173))
        else:
            self.report({'ERROR'}, "Selected bone is not the Jaw bone")

        return {'FINISHED'}

class SimsVismeaPropertyGroup(bpy.types.PropertyGroup):
    selected_bone_name: bpy.props.StringProperty(
        name="Selected Bone Name",
        description="Name of the selected bone",
        default=""
    )

class BoneTransformohOperatorold(bpy.types.Operator):
    """Moves the characher mouth to momick the sound of OH"""
    bl_idname = "object.bone_transform2"
    bl_label = "OH"
    bl_options = {'REGISTER', 'UNDO'}
    @classmethod
    def poll(cls, context):
        return is_pose_mode(context)
    def execute(self, context):
        # Get the armature object
        armature = bpy.data.objects.get("Armature")
        if not armature:
            return {'CANCELLED'}

        # Get the bones
        lower_mouth_area = armature.pose.bones.get("CAS_LowerMouthArea")
        upper_mouth_area = armature.pose.bones.get("CAS_UpperMouthArea")
        Right_Mouth = armature.pose.bones.get("R_Mouth")
        Left_Mouth = armature.pose.bones.get("L_Mouth")
        lolip = armature.pose.bones.get("LoLip")
        jaw = armature.pose.bones.get("Jaw")

        # Rotate the bones
        lower_mouth_area.rotation_euler.x += 0.0892665
        upper_mouth_area.rotation_euler.x -= 0.0892665
        Right_Mouth.location.z -= -0.0032921
        Right_Mouth.location.x -= -0.0132921
        Left_Mouth.location.z -= -0.0032921
        Left_Mouth.location.x -= 0.0132921
        lolip.location.z -= 0.0042921
        if jaw:
            jaw.rotation_quaternion.rotate(Quaternion((1, 0, 0), 0.142173))

        return {'FINISHED'}

class BoneTransformCHOperatorold(bpy.types.Operator):
    """Moves the characher mouth to momick the sound of CH"""
    bl_idname = "object.bone_transform3"
    bl_label = "Ch"
    bl_options = {'REGISTER', 'UNDO'}
    @classmethod
    def poll(cls, context):
        return is_pose_mode(context)
    def execute(self, context):
        # Get the armature object
        armature = bpy.data.objects.get("Armature")
        if not armature:
            return {'CANCELLED'}

        # Get the bones
        lower_mouth_area = armature.pose.bones.get("CAS_LowerMouthArea")
        upper_mouth_area = armature.pose.bones.get("CAS_UpperMouthArea")
        Right_Mouth = armature.pose.bones.get("R_Mouth")
        Left_Mouth = armature.pose.bones.get("L_Mouth")
        lolip = armature.pose.bones.get("LoLip")
        jaw = armature.pose.bones.get("Jaw")

        # Rotate the bones
        lower_mouth_area.rotation_euler.x += 0.0892665
        upper_mouth_area.rotation_euler.x -= 0.0892665
        #Right_Mouth.location.z -= -0.0032921
        Right_Mouth.location.x -= -0.0132921
        #Right_Mouth.location.y -= -0.010747
        #Left_Mouth.location.y -= 0.010747
        #Left_Mouth.location.z -= -0.0032921
        Left_Mouth.location.x -= 0.0132921
        lolip.location.z -= -0.0142921
        if jaw:
            jaw.rotation_quaternion.rotate(Quaternion((1, 0, 0), 0.142173))

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

class RotateLUpLidOperatorold(bpy.types.Operator):
    bl_idname = "object.rotate_l_uplid"
    bl_label = "Close Left"
    bl_options = {'REGISTER', 'UNDO'}
    @classmethod
    def poll(cls, context):
        return is_pose_mode(context)
    def execute(self, context):
        armature = bpy.data.objects.get("Armature")
        if not armature:
            return {'CANCELLED'}
        # Get the bones
        l_uplid = armature.pose.bones.get("L_UpLid")
        l_lolid = armature.pose.bones.get("L_LoLid")
        # Rotate the bones 0.349066 349066
        if l_uplid:
            l_uplid.rotation_quaternion.rotate(Quaternion((1, 0, 0), -0.349066))
        if l_lolid:
            l_lolid.rotation_quaternion.rotate(Quaternion((1, 0, 0), 0.349066))
        return {'FINISHED'}

class RotateLLoLidOperatorold(bpy.types.Operator):
    bl_idname = "object.rotate_l_lolid"
    bl_label = "Close Right"
    bl_options = {'REGISTER', 'UNDO'}
    @classmethod
    def poll(cls, context):
        return is_pose_mode(context)
    def execute(self, context):
        armature = bpy.data.objects.get("Armature")
        if not armature:
            return {'CANCELLED'}
        # Get the bones
        R_uplid = armature.pose.bones.get("R_UpLid")
        R_lolid = armature.pose.bones.get("R_LoLid")
        # Rotate the bones 0.349066 349066
        if R_uplid:
            R_uplid.rotation_quaternion.rotate(Quaternion((1, 0, 0), -0.349066))
        if R_lolid:
            R_lolid.rotation_quaternion.rotate(Quaternion((1, 0, 0), 0.349066))
        return {'FINISHED'}

class RotateBothEOperatorold(bpy.types.Operator):
    bl_idname = "object.rotatebotheye"
    bl_label = "Close Both Eyes"
    bl_options = {'REGISTER', 'UNDO'}
    @classmethod
    def poll(cls, context):
        return is_pose_mode(context)
    def execute(self, context):
        armature = bpy.data.objects.get("Armature")
        if not armature:
            return {'CANCELLED'}
        # Get the bones
        R_uplid = armature.pose.bones.get("R_UpLid")
        R_lolid = armature.pose.bones.get("R_LoLid")
        l_uplid = armature.pose.bones.get("L_UpLid")
        l_lolid = armature.pose.bones.get("L_LoLid")
        # Rotate the bones 0.349066 349066
        if R_uplid:
            R_uplid.rotation_quaternion.rotate(Quaternion((1, 0, 0), -0.349066))
        if R_lolid:
            R_lolid.rotation_quaternion.rotate(Quaternion((1, 0, 0), 0.349066))
        if l_uplid:
            l_uplid.rotation_quaternion.rotate(Quaternion((1, 0, 0), -0.349066))
        if l_lolid:
            l_lolid.rotation_quaternion.rotate(Quaternion((1, 0, 0), 0.349066))
        self.report({'INFO'}, "Both Eyes are now closed")
        return {'FINISHED'}

def menu_funcold(self, context):
    self.layout.operator(BoneTransformAAOperatorold.bl_idname)

classes = (
    SimsVismeaSoundsPanelnew,
    Objectmodeinold,
    ObjectmodeinoldSecoundold,
    Editmodeinold,
    Posemodeinold,
    BoneTransformAAOperatorold,
    BoneTransformohOperatorold,
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


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    bpy.types.VIEW3D_MT_object.remove(menu_funcold)
    bpy.utils.register_class(SimsVismeaPropertyGroup)
    bpy.types.Scene.sims_vismea_props = bpy.props.PointerProperty(type=SimsVismeaPropertyGroup)

if __name__ == "__main__":
    register()
