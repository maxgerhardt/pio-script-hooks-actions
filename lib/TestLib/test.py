Import('env', 'projenv')

def copy_firmware(source, target, env):
    print("test copy_firmware() is called")

def post_bin_action(source, target, env):
    print("test post_bin_action() is called")

def post_progsize(source, target, env):
    print("test post_progsize() is called")

for e in (env, projenv, DefaultEnvironment()):
    e.AddPostAction("buildprog", copy_firmware)
    e.AddPostAction("checkprogsize", post_progsize)
    # for Uno projects: firmware.hex
    e.AddPostAction("$BUILD_DIR/${PROGNAME}.hex", post_bin_action)
    # for other projects
    e.AddPostAction("$BUILD_DIR/${PROGNAME}.bin", post_bin_action)
print("test: script gets called")