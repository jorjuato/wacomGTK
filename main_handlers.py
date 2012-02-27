import gtk
import gtk.glade
import drawingarea

#########################################################################	
#####	CALLBACKS		#################################################
#########################################################################

global app
	
class MainHandlers:
	

######## MAIN WINDOW CALLBACKS
	def on_delete_event(self,event):
		return False
	
	def on_destroy(self):
   		gtk.main_quit()

######## TOOL BAR CALLBACKS
	def on_toolbuttonNuevo_clicked(self):
		pass
	
	def on_toolbuttonSalir_clicked(self):
		gtk.main_quit()	

	def on_toolbuttonAyuda_clicked(self):
		gladefile="gtkperiment.glade"
		windowname="aboutdialog"
		wTree=gtk.glade.XML (gladefile,windowname)
		return
		
######## TOGGLED CALLBACKS
	def on_checkbuttonHV_toggled(self):
		if app['frameHV'].get_property("sensitive") == False:
			app['frameHV'].set_sensitive(True) 
		else: 
			app['frameHV'].set_sensitive(False)
	
	def on_checkbuttonFlash_toggled(self):
		if app['frameFlash'].get_property("sensitive") == False:
			app['frameFlash'].set_sensitive(True) 
		else: 
			app['frameFlash'].set_sensitive(False)
	
	def on_checkbuttonFitt_toggled(self):
		if app['frameFitt'].get_property("sensitive") == False:
			app['frameFitt'].set_sensitive(True)
		else: 
			app['frameFitt'].set_sensitive(False)
	
	def on_checkbuttonFeed_toggled(self):
		if app['frameFeed'].get_property("sensitive") == False:
			app['frameFeed'].set_sensitive(True)
		else: 
			app['frameFeed'].set_sensitive(False)
					
######## AYUDA BUTTONS CALLBACKS	
	def on_ayuda1_clicked(self):
		gladefile="gtkperiment.glade"
		windowname="ayudaHV"
		wTree=gtk.glade.XML (gladefile,windowname)
		return
		
	def on_ayuda2_clicked(self):
		gladefile="gtkperiment.glade"
		windowname="ayudaFlash"
		wTree=gtk.glade.XML (gladefile,windowname)
		return
		
	def on_ayuda3_clicked(self):
		gladefile="gtkperiment.glade"
		windowname="ayudaFitt"
		wTree=gtk.glade.XML (gladefile,windowname)
		return
			
	def on_ayuda4_clicked(self):
		gladefile="gtkperiment.glade"
		windowname="ayudaFeed"
		wTree=gtk.glade.XML (gladefile,windowname)
		return
			
######## INICIAR BUTTONS CALLBACKS				
	def on_iniciar1_clicked(self):
		wacomDraw = drawingarea.WacomDrawWindow()
		return
			
	def on_iniciar2_clicked(self):
		wacomDraw = drawingarea.WacomDrawWindow()
		return
			
	def on_iniciar3_clicked(self):
		wacomDraw = drawingarea.WacomDrawWindow()
		return
			
	def on_iniciar4_clicked(self):
		wacomDraw = drawingarea.WacomDrawWindow()
		return



			


