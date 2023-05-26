#
# Auto-Generated file. Do not edit!
#

# Add inputs and outputs from these tool invocations to the build variables
C_SRCS += \
../libc/stdio/printf.c \
../libc/stdio/sscanf.c

OBJS += \
./libc/stdio/printf.o \
./libc/stdio/sscanf.o

C_DEPS += \
./libc/stdio/printf.d \
./libc/stdio/sscanf.d

# Each subdirectory must supply rules for building sources it contributes
libc/stdio/%.o: ../libc/stdio/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: SDE Lite C Compiler'
	D:/LoongIDE/mips-2011.03/bin/mips-sde-elf-gcc.exe -mips32 -G0 -EL -msoft-float -DLS1B -DOS_NONE  -O0 -g -Wall -c -fmessage-length=0 -pipe -I"../" -I"../include" -I"../core/include" -I"../core/mips" -I"../ls1x-drv/include" -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

