import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                           QHBoxLayout, QListWidget, QTextEdit, QLineEdit, 
                           QPushButton, QLabel, QDialog, QMessageBox, QScrollArea,
                           QSplitter, QFrame, QToolBar, QSpinBox)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QPalette, QColor, QIcon, QAction, QTextCharFormat, QTextCursor, QPixmap, QPainter
from qt_material import apply_stylesheet
from tablet_content import get_tablet_content, search_tablets

class PasswordDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("The Emerald Tablets Portal")
        self.setFixedSize(500, 400)  # Increased size to accommodate image
        
        layout = QVBoxLayout()
        layout.setSpacing(15)
        
        # Add image
        image_label = QLabel()
        pixmap = QPixmap("c:/Users/Octavian/Emerald Tablets_project/throne_thoth.png")
        scaled_pixmap = pixmap.scaled(300, 250, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        image_label.setPixmap(scaled_pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(image_label)
        
        prompt_label = QLabel("Access the secret contents of Thoth's tablets by inserting the password.")
        prompt_label.setWordWrap(True)
        prompt_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        prompt_label.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: #ffffff;
                padding: 5px;
            }
        """)
        
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setPlaceholderText("Enter password...")
        self.password_input.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border-radius: 4px;
                font-size: 14px;
                background: #2d2d2d;
                border: 1px solid #3d3d3d;
                margin: 0 50px;
            }
            QLineEdit:focus {
                border: 1px solid #50C878;
            }
        """)
        
        submit_btn = QPushButton("Access Knowledge")
        submit_btn.clicked.connect(self.check_password)
        submit_btn.setStyleSheet("""
            QPushButton {
                padding: 8px 16px;
                border-radius: 4px;
                background-color: #2d5a27;
                color: white;
                font-size: 14px;
                margin: 0 50px;
                min-height: 35px;
            }
            QPushButton:hover {
                background-color: #1e3f1b;
            }
        """)
        
        layout.addWidget(prompt_label)
        layout.addWidget(self.password_input)
        layout.addWidget(submit_btn)
        
        self.setLayout(layout)
        
        # Set dialog background color
        self.setStyleSheet("""
            QDialog {
                background-color: #1a1a1a;
            }
        """)
    
    def check_password(self):
        if self.password_input.text() == "amenti":
            self.accept()
        else:
            QMessageBox.warning(self, "Error", "Incorrect Password")

class BackgroundWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.background = QPixmap("c:/Users/Octavian/Emerald Tablets_project/wallpaper_of_thoth.png")

    def paintEvent(self, event):
        painter = QPainter(self)
        scaled_bg = self.background.scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        
        # Calculate position to right-align the image
        x = self.width() - scaled_bg.width()  # This will align to right
        y = (self.height() - scaled_bg.height()) // 2  # Keep vertical centering
        
        painter.drawPixmap(x, y, scaled_bg)

class EmeraldTabletsApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("The Emerald Tablets of Thoth")
        self.setMinimumSize(1200, 800)
        
        # Apply material theme
        apply_stylesheet(self, theme='dark_teal')
        
        # Create toolbar first
        self.create_toolbar()
        
        # Main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Header
        header = QLabel("The Emerald Tablets of Thoth")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setFont(QFont("Papyrus", 32, QFont.Weight.Bold))
        header.setStyleSheet("""
            QLabel {
                color: #50C878;
                margin-top: 15px;
                margin-bottom: 25px;
                font-family: Papyrus, 'Trajan Pro', 'Cinzel Decorative', 'Cinzel', serif;
                text-shadow: 0 0 10px #50C878,
                           0 0 20px #50C878,
                           0 0 30px #50C878,
                           2px 2px 2px rgba(0, 0, 0, 0.8);
                letter-spacing: 3px;
                font-weight: bold;
            }
        """)
        header.setMaximumHeight(80)
        layout.addWidget(header)
        
        # Main content area
        content_splitter = QSplitter(Qt.Orientation.Horizontal)
        content_splitter.setStyleSheet("""
            QSplitter {
                background: #1a1a1a;
            }
            QSplitter::handle {
                background: none;
                width: 0px;
            }
        """)
        content_splitter.setHandleWidth(0)
        content_splitter.setChildrenCollapsible(False)
        
        # Create left side container for search and navigation
        left_container = QWidget()
        left_layout = QVBoxLayout(left_container)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(0)
        
        # Search bar
        search_container = QWidget()
        search_layout = QHBoxLayout(search_container)
        search_layout.setContentsMargins(10, 0, 10, 5)
        search_container.setMaximumHeight(40)
        search_container.setFixedWidth(160)
        
        search_icon = QLabel("🔍")
        search_icon.setStyleSheet("font-size: 14px;")
        search_layout.addWidget(search_icon)
        
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search...")
        self.search_bar.setStyleSheet("""
            QLineEdit {
                padding: 5px;
                border-radius: 4px;
                font-size: 12px;
                background: #2d2d2d;
                border: 1px solid #3d3d3d;
                max-width: 120px;
            }
            QLineEdit:focus {
                border: 1px solid #50C878;
            }
        """)
        self.search_bar.textChanged.connect(self.search_content)
        search_layout.addWidget(self.search_bar)
        
        # Navigation list
        nav_container = QWidget()
        nav_container.setFixedWidth(160)
        nav_layout = QVBoxLayout(nav_container)
        nav_layout.setContentsMargins(0, 0, 0, 0)
        nav_layout.setSpacing(0)
        
        self.nav_list = QListWidget()
        self.nav_list.setFont(QFont("Cinzel", 11))
        self.nav_list.addItem("📚 Preface")
        for i in range(1, 16):
            self.nav_list.addItem(f"📜 Tablet {i}")
        self.nav_list.currentItemChanged.connect(self.show_content)
        self.nav_list.setStyleSheet("""
            QListWidget {
                background: #1a1a1a;
                border: none;
                padding: 2px;
                outline: none;
            }
            QListWidget::item {
                padding: 4px 8px;
                border-radius: 2px;
                margin: 1px 0;
                min-height: 20px;
                show-decoration-selected: 0;
            }
            QListWidget::item:selected {
                background: #2d5a27;
                color: white;
            }
            QListWidget::item:hover {
                background: #233f1e;
            }
            QScrollBar:vertical {
                background: #1a1a1a;
                width: 8px;
                margin: 0;
            }
            QScrollBar::handle:vertical {
                background: #2d5a27;
                min-height: 20px;
                border-radius: 4px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
        """)
        self.nav_list.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.nav_list.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.nav_list.setSpacing(0)
        
        nav_layout.addWidget(self.nav_list)
        
        # Add Thoth image below navigation
        image_label = QLabel()
        pixmap = QPixmap("c:/Users/Octavian/Emerald Tablets_project/thoth.png")
        scaled_pixmap = pixmap.scaled(160, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        image_label.setPixmap(scaled_pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        image_label.setStyleSheet("""
            QLabel {
                background: transparent;
                padding: 10px;
                margin-top: 10px;
            }
        """)
        nav_layout.addWidget(image_label)
        nav_layout.addStretch()
        
        # Add search and nav to left container
        left_layout.addWidget(search_container)
        left_layout.addWidget(nav_container)
        
        # Add left container to splitter
        content_splitter.addWidget(left_container)
        
        # Text display area with maximized space
        text_container = QWidget()
        text_layout = QVBoxLayout(text_container)
        text_layout.setContentsMargins(0, 0, 0, 0)
        text_layout.setSpacing(0)
        
        # Create background widget
        background = BackgroundWidget()
        
        # Create text display with transparent background
        self.text_display = QTextEdit()
        self.text_display.setReadOnly(True)
        self.text_display.setFont(QFont("Crimson Pro", 16))
        self.text_display.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.text_display.setStyleSheet("""
            QTextEdit {
                background-color: rgba(26, 26, 26, 0.4);
                color: #ffffff;
                border: none;
                padding: 40px;
                line-height: 1.6;
            }
            QScrollBar:vertical {
                background: #1a1a1a;
                width: 8px;
                margin: 0;
            }
            QScrollBar::handle:vertical {
                background: #2d5a27;
                min-height: 20px;
                border-radius: 4px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
        """)
        
        # Create a stacked layout
        stack_layout = QVBoxLayout()
        stack_layout.setContentsMargins(0, 0, 0, 0)
        stack_layout.setSpacing(0)
        
        # Add background to text container
        text_layout.addWidget(background)
        
        # Make text display fill the entire container
        self.text_display.setParent(text_container)
        text_container.resizeEvent = lambda e: self.text_display.setGeometry(0, 0, text_container.width(), text_container.height())
        
        content_splitter.addWidget(text_container)
        
        # Small copy button in bottom-right corner
        button_container = QWidget()
        button_layout = QHBoxLayout(button_container)
        button_layout.setContentsMargins(0, 0, 40, 10)
        button_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        button_container.setMaximumHeight(35)
        
        copy_button = QPushButton("Copy")
        copy_button.setFixedSize(60, 25)
        copy_button.setStyleSheet("""
            QPushButton {
                background: #2d5a27;
                color: white;
                border-radius: 3px;
                font-size: 12px;
            }
            QPushButton:hover {
                background: #233f1e;
            }
        """)
        copy_button.clicked.connect(self.copy_selected_text)
        button_layout.addWidget(copy_button)
        text_layout.addWidget(button_container)
        
        # Set fixed sizes for splitter sections
        content_splitter.setSizes([160, self.width() - 160])  # Fix initial sizes
        content_splitter.setStretchFactor(0, 0)  # Make first section fixed
        content_splitter.setStretchFactor(1, 1)  # Make second section stretch
        
        layout.addWidget(content_splitter, 1)
    
    def create_toolbar(self):
        toolbar = QToolBar()
        toolbar.setMovable(False)
        toolbar.setStyleSheet("""
            QToolBar {
                spacing: 10px;
                padding: 5px;
                background: transparent;
            }
            QSpinBox {
                background: #2d2d2d;
                color: white;
                border: 1px solid #3d3d3d;
                padding: 5px;
                border-radius: 4px;
                width: 50px;
            }
            QLabel {
                color: white;
            }
        """)
        
        # Font size control
        font_size_label = QLabel("Font Size:")
        toolbar.addWidget(font_size_label)
        
        self.font_size = QSpinBox()
        font_size = QSpinBox()
        font_size.setRange(12, 24)
        font_size.setValue(16)
        font_size.valueChanged.connect(self.change_font_size)
        toolbar.addWidget(font_size)
        
        self.addToolBar(toolbar)
    
    def change_font_size(self, size):
        self.text_display.setFont(QFont("Crimson Pro", size))
        # Refresh the current content to update font size
        current_item = self.nav_list.currentItem()
        if current_item:
            self.show_content(current_item, None)
    
    def copy_selected_text(self):
        cursor = self.text_display.textCursor()
        if cursor.hasSelection():
            text = cursor.selectedText()
            QApplication.clipboard().setText(text)
            QMessageBox.information(self, "Success", "Text copied to clipboard!")
    
    def search_content(self, text):
        if not text:
            for i in range(self.nav_list.count()):
                self.nav_list.item(i).setHidden(False)
            return
        
        results = search_tablets(text)
        
        # Update navigation list visibility
        for i in range(self.nav_list.count()):
            item = self.nav_list.item(i)
            item_text = item.text().replace("📚 ", "").replace("📜 ", "")
            item.setHidden(item_text not in results)
        
        # Show search results with highlighting
        if results:
            result_text = ["<div style='color: #ffffff;'>"]
            for tablet_name, matches in results.items():
                result_text.append(f"<h2 style='color: #50C878; margin: 20px 0; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);'>{tablet_name}</h2>")
                for match in matches:
                    highlighted_match = match.replace(text, f"<span style='background-color: #2d5a27; padding: 2px 4px; border-radius: 3px;'>{text}</span>")
                    result_text.append(f"<div style='margin: 10px 0; line-height: 1.6;'>{highlighted_match}</div>")
            result_text.append("</div>")
            
            self.text_display.setHtml("\n".join(result_text))
        else:
            self.text_display.setHtml("<div style='color: #ffffff; text-align: center; margin-top: 40px;'>No matches found.</div>")
    
    def show_content(self, current, previous):
        if not current:
            return
        
        tablet_name = current.text().replace("📚 ", "").replace("📜 ", "")
        content = get_tablet_content(tablet_name)
        if content:
            formatted_content = f"""<div style='color: #ffffff; padding: 40px 40px 20px 40px;'>
                <div style='font-size: {self.text_display.font().pointSize()}px; line-height: 1.8; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);'>
                    {content.replace('\n\n', f'</div><div style="margin: 20px 0; font-size: {self.text_display.font().pointSize()}px; line-height: 1.8; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">')}
                </div>
            </div>"""
            
            self.text_display.setHtml(formatted_content)
        else:
            self.text_display.setText(f"Content for {tablet_name} is not available.")

def main():
    app = QApplication(sys.argv)
    
    # Show password dialog
    password_dialog = PasswordDialog()
    if password_dialog.exec() != QDialog.DialogCode.Accepted:
        sys.exit()
    
    # Show main window
    window = EmeraldTabletsApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 