from visualiser import app

def test_01_header(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_text_to_equal("#header", timeout=15)

def test_02_visualisation(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#salesGraph", timeout=15)

def test_03_region(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region", timeout=15)