bl_info = {
    "name" : "VRCVismeaBones",
    "author" : "A7med9870",
    "description" : "Create visemes faster for VRChat, with your rigged models",
    "blender" : (3, 3, 0),
    "version" : (0, 0, 2,1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Object"
}

import bpy
from mathutils import Quaternion
from bpy.types import Panel, AddonPreferences
from bpy.props import BoolProperty, EnumProperty
try:
    # from . import listtheviesma
    from . import applypart
    from . import Oldbonetransfrom
    from . import Newbonetransfrom
    from . import Changemodespanmel
except Exception as e:
    print("Error loading file:", e)

class VRCvvv(bpy.types.AddonPreferences):
    bl_idname = __name__

    show_shapekeylist_panel: bpy.props.BoolProperty(
        name="Show Listing ShapeKeys custom panel",
        description="A panel on the side, to see what shapekeys you have; still on buggy state",
        default=False,
        update=lambda self, context: context.area.tag_redraw(),
    )
    documentation_url: bpy.props.StringProperty(
        name="Documentation URL",
        description="URL for the addon documentation",
        default="https://github.com/A7med9870/Blender-Car-Streamliner",
    )
    YT_url: bpy.props.StringProperty(
        name="YT URL",
        description="URL for the Creator Youtube",
        default="https://www.youtube.com/channel/UCMbA857nJ9w5FzfjrhBzq8A",
    )
    IG_url: bpy.props.StringProperty(
        name="IG URL",
        description="URL for the Creator Instagram",
        default="https://www.instagram.com/a7hmed9870/reels/?hl=en",
    )
    Boners_enum1: EnumProperty(
        name="Bones Mover",
        description="For more compactily",
        items=[
            ("OPTION1", "New Boner (dynamic bones chooser)", "Hardcoded, as in you need the bones to match the names to work"),
            ("OPTION2", "Old Bone Movers (only for sims 4 characters)", "You will need to edit the files in order to get the result you want"),
        ],
        default="OPTION2"
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "Boners_enum1")

        row = layout.row()
        row.prop(self, "show_shapekeylist_panel")

        layout.prop(self, "FBXEdropdown_enum1")

        row = layout.row()
        row.operator("wm.url_open", text="Github Page").url = self.documentation_url
        row.operator("wm.url_open", text="Creator's Youtube").url = self.YT_url
        row.operator("wm.url_open", text="Creator's Instagram").url = self.IG_url

        layout.label(text="Thanks for Testing the addon!")
        layout.label(text="This addon was made to help with porting sims 4 charcaters orignally")
        layout.label(text="But then was almost fully redsgined to be useable with any different skelatal")
        layout.label(text="model that is rigged, and has bones to define the mouth and eys, just needs")
        layout.label(text="a fast way to create blendshape for VRChat characters")


    def invoke(self, context, event):
        import webbrowser
        webbrowser.open(self.documentation_url)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(VRCvvv)
    applypart.register()
    Oldbonetransfrom.register()
    Newbonetransfrom.register()
    Changemodespanmel.register()
    # listtheviesma.register()

def unregister():
    bpy.utils.unregister_class(VRCvvv)
    applypart.unregister()
    Oldbonetransfrom.unregister()
    Newbonetransfrom.unregister()
    Changemodespanmel.unregister()
    # listtheviesma.unregister()

if __name__ == "__main__":
    register()
