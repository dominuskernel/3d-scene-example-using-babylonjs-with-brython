from browser import document as doc
from browser import window
from javascript import JSObject,JSConstructor

class CreateScene:
  def __init__(self):
    self.canvas = doc["renderCanvas"]
    self.BABYLON = window.BABYLON
    engineC = JSConstructor(self.BABYLON.Engine)
    self.engine = engineC(self.canvas, True)
    sceneC = JSConstructor(self.BABYLON.Scene)
    self.scene = sceneC(self.engine)

  def camera(self):
    color3 = JSConstructor(self.BABYLON.Color3)
    self.scene.clearColor = color3(0, 1, 0)
    cameraC = JSConstructor(self.BABYLON.FreeCamera)
    self.vector3 = JSConstructor(self.BABYLON.Vector3)
    self.camera = cameraC("camera", self.vector3(0, 5, -10), self.scene)
    vector3Zero = JSConstructor(self.BABYLON.Vector3.Zero)
    self.camera.setTarget(vector3Zero())
    self.scene.activeCamera = self.camera
    self.camera.attachControl(self.canvas)

  def light(self):
    hemiC = JSConstructor(self.BABYLON.HemisphericLight)
    self.hemi = hemiC("light1", self.vector3(0,1,0), self.scene)
    self.hemi.intensity = 0.5


  def mesh(self):
    sphereC = JSConstructor(self.BABYLON.Mesh.CreateSphere)
    groundC = JSConstructor(self.BABYLON.Mesh.CreateGround)
    self.sphere = sphereC("sphere1", 16, 2, self.scene)
    self.sphere.position.y = 1
    self.ground = groundC("ground1", 6, 6, 2, self.scene)

  def render(self):
    self.engine.runRenderLoop(self.__startScene)

  def __startScene(self):
    self.scene.render()

  def run(self):
    self.camera()
    self.light()
    self.mesh()
    self.render()

app = CreateScene()
app.run()


