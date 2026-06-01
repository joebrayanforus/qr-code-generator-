📄 Datei 1 — mux_8_1.v (das eigentliche MUX‑Modul)
verilog
module mux_8_1 (
    input  [7:0] data,
    input  [2:0] sel,
    output       Y
);

    assign Y = data[sel];

endmodule
📄 Datei 2 — top_mux8.v (Top‑Level für das Board)
⚠ Wichtig: Ports müssen EXAKT zu deinem XDC passen.

verilog
module top_mux8 (
    input  [7:0] sw,     // slide switches
    input  [2:0] btn,    // push buttons
    output       led0    // green LED
);

    wire y;

    mux_8_1 dut (
        .data(sw),
        .sel(btn),
        .Y(y)
    );

    assign led0 = y;

endmodule
⭐ Étape 3 — XDC anpassen
Du hast ein großes Master‑XDC.
Für dieses Projekt brauchst du nur 1 Zeile ändern:

Ändere:
Code
[get_ports { led[0] }]
Zu:
Code
[get_ports { led0 }]
Alles andere bleibt unverändert.

⭐ Étape 4 — Simulation hinzufügen
Du brauchst eine Simulation Source:

📄 Datei 3 — mux_8_1_tb.v (Testbench)
verilog
`timescale 1ns / 1ps

module mux_8_1_tb;

    reg  [7:0] data;
    reg  [2:0] sel;
    wire       Y;

    mux_8_1 dut (
        .data(data),
        .sel(sel),
        .Y(Y)
    );

    initial begin
        data = 8'b1010_1101;

        sel = 3'b000; #10;
        sel = 3'b001; #10;
        sel = 3'b010; #10;
        sel = 3'b011; #10;
        sel = 3'b100; #10;
        sel = 3'b101; #10;
        sel = 3'b110; #10;
        sel = 3'b111; #10;

        $stop;
    end

endmodule
Erstellt von Joebrayan Forus, Informatikstudent an der Universität Siegen. Lizenz: MIT – frei zur Nutzung und Erweiterung mit Namensnennung.
