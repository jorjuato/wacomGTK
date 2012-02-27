######## DRAWING AREA CALLBACKS
class DrawHandlers:

	def ConfigureEvent(self, widget, event):
		pass		

	def GetPressure(self):
		dev = gtk.gdk.devices_list()[self.Device]
		state = dev.get_state(self.window)
		return dev.get_axis(state[0], gtk.gdk.AXIS_PRESSURE)
	
	def MotionEvent(self, widget, event):
		if self.Drawing:
			x, y = event.get_coords()
			p = self.GetPressure()
			if p == None:
				p = 0.0
			r =  p * 50 + 5
			#colormap = widget.get_colormap()
			#color = colormap.alloc_color(r, 0, 0, writeable=False, best_match=True)
			#gc.foreground = color
			self.window.draw_line(gc, self.oldx, self.oldy, x, y)
			self.oldx = x
			self.oldy = y
	
	def ButtonPress(self, widget, event):
		self.Drawing = True
		self.oldx, self.oldy = event.get_coords()

	def ButtonRelease(self, widget, event):
		self.Drawing = False
		pass

	def ExposeEvent(self, widget, event):
		widget.draw()
		return False

