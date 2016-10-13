Import("env")

env.Replace(
    SETFUSECMD='$UPLOADER $UPLOADERFLAGS -P $UPLOAD_PORT -b $UPLOAD_SPEED -e -Ulock:w:0x3F:m -Uefuse:w:0x05:m -Uhfuse:w:0xDA:m -Ulfuse:w:0xE2:m',
    UPLOADBOOTCMD='$UPLOADER $UPLOADERFLAGS -P $UPLOAD_PORT -b $UPLOAD_SPEED -Uflash:w:$SOURCES:i -Ulock:w:0x0F:m'
)

bootloader_path = './bootloader/ATmegaBOOT_168_atmega328_pro_8MHz.hex'
uploadboot = env.Alias(
    "uploadboot", bootloader_path,
    [env.VerboseAction(env.AutodetectUploadPort, "Looking for upload port..."),
     env.VerboseAction("$SETFUSECMD", "Setting fuses"),
     env.VerboseAction("$UPLOADBOOTCMD", "Uploading bootloader $SOURCE")])
AlwaysBuild(uploadboot)
