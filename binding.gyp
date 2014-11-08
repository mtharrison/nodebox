{
    "targets": [{
      "target_name": "nodebox", 
      "conditions": [],
      "dependencies": [
            "<(module_root_dir)/deps/Box2D/libBox2d.gyp:Box2D"
      ],
      "include_dirs"  : [
            "<!(node -e \"require('nan')\")"
      ],
      "sources": [ "nodebox.cpp" ]
    }]
}