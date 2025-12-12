# AI Created class for making a Tkinter widget draggable and resizable.


class DraggableWidget:
    def __init__(self, widget, resize_border=8):
        self.widget = widget
        self.resize_border = resize_border
        self.resizing = False
        self.dragging = False

        # Bind for dragging and resizing
        widget.bind("<Motion>", self.on_motion)
        widget.bind("<ButtonPress-1>", self.on_press)
        widget.bind("<B1-Motion>", self.on_drag_or_resize)
        widget.bind("<ButtonRelease-1>", self.on_release)

    def on_motion(self, event):
        """Detect if cursor is near the border for resizing"""
        w, h = self.widget.winfo_width(), self.widget.winfo_height()
        x, y = event.x, event.y

        border = self.resize_border
        near_right = abs(x - w) <= border
        near_bottom = abs(y - h) <= border

        # Only resize from bottom-right corner (for simplicity)

        try:
            if near_right and near_bottom:
                self.widget.config(cursor="bottom_right_corner")
                self.in_resize_zone = True
            else:
                self.widget.config(cursor="")
                self.in_resize_zone = False
        except:
            if near_right and near_bottom:
                self.widget.configure(cursor="bottom_right_corner")
                self.in_resize_zone = True
            else:
                self.widget.configure(cursor="")
                self.in_resize_zone = False

    def on_press(self, event):
        """Start dragging or resizing"""
        if getattr(self, "in_resize_zone", False):
            # Start resize
            self.resizing = True
            self.start_w = self.widget.winfo_width()
            self.start_h = self.widget.winfo_height()
            self.start_x = event.x_root
            self.start_y = event.y_root
        else:
            # Start drag
            self.dragging = True
            self.start_offset_x = event.x
            self.start_offset_y = event.y

    def on_drag_or_resize(self, event):
        """Handle both dragging and resizing"""
        if self.resizing:
            dx = event.x_root - self.start_x
            dy = event.y_root - self.start_y
            new_w = max(50, self.start_w + dx)
            new_h = max(50, self.start_h + dy)
            self.widget.place(width=new_w, height=new_h)
        elif self.dragging:
            x = self.widget.winfo_x() - self.start_offset_x + event.x
            y = self.widget.winfo_y() - self.start_offset_y + event.y
            self.widget.place(x=x, y=y)

    def on_release(self, event):
        """Stop any active actions"""
        self.resizing = False
        self.dragging = False
