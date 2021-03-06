"""
tracenolock test - with graphics because this is a model for analysis
"""

cases = [
    ('Generate FSM for simple program with two threads: listfiles, openfile',
     'pma.py tracenolock'),

    ('Generate graphics',
     'pmg.py tracenolockFSM'),

    ('Generate an SVG file you can display in a browser',
     'dotsvg tracenolockFSM'),
]
