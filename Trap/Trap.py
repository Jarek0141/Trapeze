
import units

def createMyFeature(ag):
    ExtAPI.CreateFeature("BoxFeature")

def generateBoxGeometry(feature,fct):
	ExtAPI.Log.WriteMessage("Generating MyFeature...")
    
    # Collect all property values in meter unit
	fromUnit, toUnit = ExtAPI.DataModel.CurrentUnitFromQuantityName("Length"), "m"
    
    #Get Length width and Thickness of the Box
	LowEdge = units.ConvertUnit(feature.Properties["LowEdge"].Value, fromUnit, toUnit)
	HighEdge = units.ConvertUnit(feature.Properties["HighEdge"].Value, fromUnit, toUnit)
	High = units.ConvertUnit(feature.Properties["High"].Value, fromUnit, toUnit)
	Sdvig = units.ConvertUnit(feature.Properties["Sdvig"].Value, fromUnit, toUnit)
	Width = units.ConvertUnit(feature.Properties["Width"].Value, fromUnit, toUnit)
    
	ExtAPI.Log.WriteMessage(LowEdge.ToString())
	ExtAPI.Log.WriteMessage(HighEdge.ToString())
	ExtAPI.Log.WriteMessage(High.ToString())
	ExtAPI.Log.WriteMessage(Sdvig.ToString())
	ExtAPI.Log.WriteMessage(Width.ToString())
	
	x1=0.
	y1=0.
	x2=Sdvig
	y2=High
	x3=Sdvig+LowEdge
	y3=High
	x4=HighEdge
	y4=0.
    
	bodies=[]
	builder = ExtAPI.DataModel.GeometryBuilder
	points_list = [0.,0.,0., Sdvig,High,0., Sdvig+LowEdge,High,0., HighEdge,0.,0.]
        #Creating Box
	length = Sdvig
	bodies = []
	builder = ExtAPI.DataModel.GeometryBuilder
	polygon=builder.Primitives.Sheet.CreatePolygon(points_list)
	polygon_generated = polygon.Generate()
	extrude = builder.Operations.CreateExtrudeOperation([0.,0.,1.],Width)
	bodies.Add(extrude.ApplyTo(polygon_generated)[0])
	feature.Bodies = bodies
	feature.MaterialType = MaterialTypeEnum.Add

	feature.Bodies = bodies
	feature.MaterialType = MaterialTypeEnum.Freeze

	return True
