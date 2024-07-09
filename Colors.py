from tkinter import*
import random







list_c =[
    "#8ecae6",
    "#219ebc",
    "#023047",
    "#ffb703",
    "#fb8500",
    "#606c38",
    "#283618",
    "#fefae0",
    "#dda15e",
    "#bc6c25",
    "#cdb4db",
    "#ffc8dd",
    "#ffafcc",
    "#bde0fe",
    "#a2d2ff",
    "#dad7cd",
    "#a3b18a",
    "#588157",
    "#3a5a40",
    "#344e41",
    "#264653",
    "#2a9d8f",
    "#e9c46a",
    "#f4a261",
    "#e76f51",
    "#ffbe0b",
    "#fb5607",
    "#ff006e",
    "#8338ec",
    "#3a86ff",
    "#780000",
    "#c1121f",
    "#fdf0d5",
    "#003049",
    "#669bbc",
    "#000000",
    "#14213d",
    "#fca311",
    "#e5e5e5",
    "#ffffff",
    "#ffe5ec",
    "#ffc2d1",
    "#ffb3c6",
    "#ff8fab",
    "#fb6f92",
    "#f6bd60",
    "#f7ede2",
    "#f5cac3",
    "#84a59d",
    "#f28482",
    "#fffcf2",
    "#ccc5b9",
    "#403d39",
    "#252422",
    "#eb5e28",
    "#006d77",
    "#83c5be",
    "#edf6f9",
    "#ffddd2",
    "#e29578",
    "#a8d5e2",
    "#f9a620",
    "#ffd449",
    "#548c2f",
    "#104911",
    "#ffd6ff",
    "#e7c6ff",
    "#c8b6ff",
    "#b8c0ff",
    "#bbd0ff",
    "#003049",
    "#d62828",
    "#f77f00",
    "#fcbf49",
    "#eae2b7",
    "#22223b",
    "#4a4e69",
    "#9a8c98",
    "#c9ada7",
    "#f2e9e4",
    "#386641",
    "#6a994e",
    "#a7c957",
    "#f2e8cf",
    "#bc4749",
    "#ff9f1c",
    "#ffbf69",
    "#ffffff",
    "#cbf3f0",
    "#2ec4b6",
    "#ff99c8",
    "#fcf6bd",
    "#d0f4de",
    "#a9def9",
    "#e4c1f9",
    "#22577a",
    "#38a3a5",
    "#57cc99",
    "#80ed99",
    "#c7f9cc",
    "#cad2c5",
    "#84a98c",
    "#52796f",
    "#354f52",
    "#2f3e46",
    "#70d6ff",
    "#ff70a6",
    "#ff9770",
    "#ffd670",
    "#e9ff70",
    "#f72585",
    "#7209b7",
    "#3a0ca3",
    "#4361ee",
    "#4cc9f0",
    "#d00000",
    "#ffba08",
    "#3f88c5",
    "#032b43",
    "#136f63",
    "#0d1b2a",
    "#1b263b",
    "#415a77",
    "#778da9",
    "#e0e1dd",
    "#27187e",
    "#758bfd",
    "#aeb8fe",
    "#f1f2f6",
    "#ff8600",
    "#d8e2dc",
    "#ffe5d9",
    "#ffcad4",
    "#f4acb7",
    "#9d8189",
    "#8cb369",
    "#f4e285",
    "#f4a259",
    "#5b8e7d",
    "#bc4b51",
    "#0081a7",
    "#00afb9",
    "#fdfcdc",
    "#fed9b7",
    "#f07167",
    "#335c67",
    "#fff3b0",
    "#e09f3e",
    "#9e2a2b",
    "#540b0e",
    "#233d4d",
    "#fe7f2d",
    "#fcca46",
    "#a1c181",
    "#619b8a",
    "#008000",
    "#38b000",
    "#70e000",
    "#9ef01a",
    "#ccff33",
    "#2d6a4f",
    "#40916c",
    "#52b788",
    "#74c69d",
    "#95d5b2",
    "#0fa3b1",
    "#b5e2fa",
    "#f9f7f3",
    "#eddea4",
    "#f7a072",
    "#8e9aaf",
    "#cbc0d3",
    "#efd3d7",
    "#feeafa",
    "#dee2ff",
    "#2c6e49",
    "#4c956c",
    "#fefee3",
    "#ffc9b9",
    "#d68c45",
    "#00a6fb",
    "#0582ca",
    "#006494",
    "#003554",
    "#051923",
    "#edafb8",
    "#f7e1d7",
    "#dedbd2",
    "#b0c4b1",
    "#4a5759",
    "#004e64",
    "#00a5cf",
    "#9fffcb",
    "#25a18e",
    "#7ae582",
    "#f9dbbd",
    "#ffa5ab",
    "#da627d",
    "#a53860",
    "#450920",
    "#00916e",
    "#feefe5",
    "#ffcf00",
    "#ee6123",
    "#fa003f",
    "#2e294e",
    "#efbcd5",
    "#be97c6",
    "#8661c1",
    "#4b5267",
    "#820263",
    "#d90368",
    "#eadeda",
    "#2e294e",
    "#ffd400",
    "#355070",
    "#6d597a",
    "#b56576",
    "#e56b6f",
    "#eaac8b",
    "#353535",
    "#3c6e71",
    "#ffffff",
    "#d9d9d9",
    "#284b63",
    "#ffb5a7",
    "#fcd5ce",
    "#f8edeb",
    "#f9dcc4",
    "#fec89a",
    "#227c9d",
    "#17c3b2",
    "#ffcb77",
    "#fef9ef",
    "#fe6d73",
    "#7c6a0a",
    "#babd8d",
    "#ffdac6",
    "#fa9500",
    "#eb6424",
    "#ffe74c",
    "#ff5964",
    "#ffffff",
    "#6bf178",
    "#35a7ff",
    "#780116",
    "#f7b538",
    "#db7c26",
    "#d8572a",
    "#c32f27",
    "#8cb369",
    "#f4e285",
    "#f4a259",
    "#5b8e7d",
    "#bc4b51",
    "#d3f8e2",
    "#e4c1f9",
    "#f694c1",
    "#ede7b1",
    "#a9def9",
    "#d4e09b",
    "#f6f4d2",
    "#cbdfbd",
    "#f19c79",
    "#a44a3f",
    "#f7c59f",
    "#2a324b",
    "#767b91",
    "#c7ccdb",
    "#e1e5ee",
    "#73eedc",
    "#73c2be",
    "#776885",
    "#5f1a37",
    "#04030f",
    "#642ca9",
    "#ff36ab",
    "#ff74d4",
    "#ffb8de",
    "#ffdde1",
    "#2c6e49",
    "#4c956c",
    "#fefee3",
    "#ffc9b9",
    "#d68c45",
    "#d88c9a",
    "#f2d0a9",
    "#f1e3d3",
    "#99c1b9",
    "#8e7dbe",
    "#5465ff",
    "#788bff",
    "#9bb1ff",
    "#bfd7ff",
    "#e2fdff",
    "#2e5266",
    "#6e8898",
    "#9fb1bc",
    "#d3d0cb",
    "#e2c044",  
    "#ccd5ae",
    "#e9edc9",
    "#fefae0",
    "#faedcd",
    "#d4a373",
    "#000814",
    "#001d3d",
    "#003566",
    "#ffc300",
    "#ffd60a",
    "#ffcdb2",
    "#ffb4a2",
    "#e5989b",
    "#b5838d",
    "#6d6875",
    "#edede9",
    "#d6ccc2",
    "#f5ebe0",
    "#e3d5ca",
    "#d5bdaf",
    "#0077b6",
    "#0096c7",
    "#00b4d8",
    "#48cae4",
    "#90e0ef",
    "#132a13",
    "#31572c",
    "#4f772d",
    "#90a955",
    "#ecf39e",
    "#9b5de5",
    "#f15bb5",
    "#fee440",
    "#00bbf9",
    "#00f5d4",
    "#9d0208",
    "#d00000",
    "#dc2f02",
    "#f48c06",
    "#faa307",
    "#001524",
    "#15616d",
    "#ffecd1",
    "#ff7d00",
    "#78290f",
    "#f4f1de",
    "#e07a5f",
    "#3d405b",
    "#81b29a",
    "#f2cc8f",
    "#3d348b",
    "#7678ed",
    "#f7b801",
    "#f18701",
    "#f35b04",
    "#355070",
    "#6d597a",
    "#b56576",
    "#e56b6f",
    "#eaac8b",
    "#463f3a",
    "#8a817c",
    "#bcb8b1",
    "#f4f3ee",
    "#e0afa0",
    "#2b2d42",
    "#8d99ae",
    "#edf2f4",
    "#ef233c",
    "#d90429",
    "#d4e09b",
    "#f6f4d2",
    "#cbdfbd",
    "#f19c79",
    "#a44a3f",
    "#343a40",
    "#495057",
    "#6c757d",
    "#adb5bd",
    "#ced4da",
    "#7f4f24",
    "#936639",
    "#a68a64",
    "#b6ad90",
    "#c2c5aa",
    "#4f000b",
    "#720026",
    "#ce4257",
    "#ff7f51",
    "#ff9b54",
    "#e63946",
    "#f1faee",
    "#a8dadc",
    "#457b9d",
    "#1d3557",
    "#353535",
    "#3c6e71",
    "#ffffff",
    "#d9d9d9",
    "#284b63",
    "#e7ecef",
    "#274c77",
    "#6096ba",
    "#a3cef1",
    "#8b8c89",
    "#6f1d1b",
    "#bb9457",
    "#432818",
    "#99582a",
    "#ffe6a7",
    "#335c67",
    "#fff3b0",
    "#e09f3e",
    "#9e2a2b",
    "#540b0e",
    "#00c3ff",
    "#e84800",
    "#6d0505",
    "#c10f05",
    "#ffef00",
    "#5f0f40",
    "#9a031e",
    "#fb8b24",
    "#e36414",
    "#0f4c5c",
    "#edeec9",
    "#dde7c7",
    "#bfd8bd",
    "#98c9a3",
    "#77bfa3",
    "#800f2f",
    "#a4133c",
    "#c9184a",
    "#ff4d6d",
    "#ff758f",
    "#bee9e8",
    "#62b6cb",
    "#1b4965",
    "#cae9ff",
    "#5fa8d3",
    "#8cb369",
    "#f4e285",
    "#f4a259",
    "#5b8e7d",
    "#bc4b51",
    "#7400b8",
    "#6930c3",
    "#5e60ce",
    "#5390d9",
    "#4ea8de",
    "#0081a7",
    "#00afb9",
    "#fdfcdc",
    "#fed9b7",
    "#f07167",
    "#390099",
    "#9e0059",
    "#ff0054",
    "#ff5400",
    "#ffbd00",
    "#ffffff",
    "#00171f",
    "#003459",
    "#007ea7",
    "#00a8e8",
    "#0a9396",
    "#94d2bd",
    "#e9d8a6",
    "#ee9b00",
    "#ae2012",
    "#cb997e",
    "#ddbea9",
    "#ffe8d6",
    "#b7b7a4",
    "#a5a58d",
    "#95d5b2",
    "#74c69d",
    "#52b788",
    "#40916c",
    "#2d6a4f",
    "#1565c0",
    "#1976d2",
    "#1e88e5",
    "#2196f3",
    "#42a5f5",
    "#231942",
    "#5e548e",
    "#9f86c0",
    "#be95c4",
    "#e0b1cb",
    "#2d7dd2",
    "#97cc04",
    "#eeb902",
    "#f45d01",
    "#474647",
    "#02010a",
    "#04052e",
    "#140152",
    "#22007c",
    "#0d00a4",
    "#c9cba3",
    "#ffe1a8",
    "#e26d5c",
    "#723d46",
    "#472d30",
    "#8ecae6",
    "#219ebc",
    "#023047",
    "#ffc803",
    "#fa0070",
    "#f08080",
    "#f4978e",
    "#f8ad9d",
    "#fbc4ab",
    "#ffdab9",
    "#d8e2dc",
    "#ffffff",
    "#ffcad4",
    "#f4acb7",
    "#9d8189",
    "#080708",
    "#3772ff",
    "#df2935",
    "#fdca40",
    "#e6e8e6",
    "#0b3954",
    "#087e8b",
    "#bfd7ea",
    "#ff5a5f",
    "#c81d25",
    "#ffffff",
    "#84dcc6",
    "#a5ffd6",
    "#ffa69e",
    "#ff686b",
    "#022b3a",
    "#1f7a8c",
    "#bfdbf7",
    "#e1e5f2",
    "#ffffff",
    "#585123",
    "#eec170",
    "#f2a65a",
    "#f58549",
    "#772f1a",
    "#461220",
    "#8c2f39",
    "#b23a48",
    "#fcb9b2",
    "#fed0bb",
    "#5affe7",
    "#08c6ab",
    "#01c38d",
    "#726eff",
    "#132d46",
    "#edae49",
    "#d1495b",
    "#00798c",
    "#30638e",
    "#003d5b",
    "#b9d6f2",
    "#061a40",
    "#0353a4",
    "#006daa",
    "#003559",
    "#031d44",
    "#04395e",
    "#70a288",
    "#dab785",
    "#d5896f",
    "#fbfbf2",
    "#e5e6e4",
    "#cfd2cd",
    "#a6a2a2",
    "#847577",
    "#9c89b8",
    "#f0a6ca",
    "#efc3e6",
    "#f0e6ef",
    "#b8bedd",
    "#06154f",
    "#8a94db",
    "#fcf7e0",
    "#553b72",
    "#e1d9ef",
    "#ff9100",
    "#ff9100",
    "#240046",
    "#3c096c",
    "#5a189a",
    "#f0ead2",
    "#dde5b6",
    "#adc178",
    "#a98467",
    "#6c584c",
    "#03045e",
    "#0077b6",
    "#00b4d8",
    "#90e0ef",
    "#caf0f8",
    "#201e1f",
    "#ff4000",
    "#faaa8d",
    "#feefdd",
    "#50b2c0",
    "#0d3b66",
    "#faf0ca",
    "#f4d35e",
    "#ee964b",
    "#f95738",
    "#001427",
    "#708d81",
    "#f4d58d",
    "#bf0603",
    "#8d0801",
    "#0d1321",
    "#1d2d44",
    "#3e5c76",
    "#748cab",
    "#f0ebd8",
    "#0a1128",
    "#001f54",
    "#034078",
    "#1282a2",
    "#fefcfb",
    "#ede0d4",
    "#e6ccb2",
    "#b08968",
    "#7f5539",
    "#9c6644",
    "#ff7b00",
    "#ff8800",
    "#ff9500",
    "#ffa200",
    "#ffaa00",
    "#642ca9",
    "#ff36ab",
    "#ff74d4",
    "#ffb8de",
    "#ffdde1",
    "#ee6055",
    "#60d394",
    "#aaf683",
    "#ffd97d",
    "#ff9b85",
    "#050505",
    "#1b9aaa",
    "#dddbcb",
    "#f5f1e3",
    "#ffffff",
    "#603808",
    "#6f4518",
    "#8b5e34",
    "#a47148",
    "#d4a276",
    "#f94144",
    "#f9844a",
    "#f9c74f",
    "#90be6d",
    "#277da1",
    "#471ca8",
    "#884ab2",
    "#ff930a",
    "#f24b04",
    "#d1105a",
    "#64113f",
    "#de4d86",
    "#f29ca3",
    "#f7cacd",
    "#84e6f8",
    "#05668d",
    "#028090",
    "#00a896",
    "#02c39a",
    "#f0f3bd",
    "#0a0908",
    "#22333b",
    "#f2f4f3",
    "#a9927d",
    "#5e503f",
    "#9381ff",
    "#b8b8ff",
    "#f8f7ff",
    "#ffeedd",
    "#ffd8be",
    "#7bdff2",
    "#b2f7ef",
    "#eff7f6",
    "#f7d6e0",
    "#f2b5d4",
    "#e6b3b0",
    "#dc94ac",
    "#6b4f99",
    "#3f418b",
    "#162a4f",
    "#00296b",
    "#003f88",
    "#00509d",
    "#fdc500",
    "#ffd500",
    "#fff1e6",
    "#f0efeb",
    "#ddbea9",
    "#a5a58d",
    "#b7b7a4",
    "#90f1ef",
    "#ffd6e0",
    "#ffef9f",
    "#c1fba4",
    "#7bf1a8",
    "#ef476f",
    "#ffd166",
    "#06d6a0",
    "#118ab2",
    "#073b4c",
    "#fcaa67",
    "#b0413e",
    "#ffffc7",
    "#548687",
    "#473335",
    "#f1dac4",
    "#a69cac",
    "#474973",
    "#161b33",
    "#0d0c1d",
    "#083d77",
    "#ebebd3",
    "#f4d35e",
    "#ee964b",
    "#f95738",
    "#73877b",
    "#839788",
    "#bdbbb6",
    "#e5d1d0",
    "#f5e4d7",
    "#813405",
    "#d45113",
    "#f9a03f",
    "#f8dda4",
    "#ddf9c1",
    "#caffbf",
    "#9bf6ff",
    "#a0c4ff",
    "#bdb2ff",
    "#ffc6ff",
    "#ff4800",
    "#ff5400",
    "#ff6000",
    "#ff6d00",
    "#ff7900",
    "#ef6351",
    "#f38375",
    "#f7a399",
    "#fbc3bc",
    "#ffe3e0",
    "#1a535c",
    "#4ecdc4",
    "#f7fff7",
    "#ff6b6b",
    "#ffe66d",
    "#393d3f",
    "#fdfdff",
    "#c6c5b9",
    "#62929e",
    "#546a7b",
    "#ff6b35",
    "#f7c59f",
    "#efefd0",
    "#004e89",
    "#1a659e",
    "#ffd9da",
    "#ea638c",
    "#89023e",
    "#30343f",
    "#1b2021",
    "#fe938c",
    "#e6b89c",
    "#ead2ac",
    "#9cafb7",
    "#4281a4",
    "#01161e",
    "#124559",
    "#598392",
    "#aec3b0",
    "#eff6e0",
    "#3a2e39",
    "#1e555c",
    "#f4d8cd",
    "#edb183",
    "#f15152",
    "#545e75",
    "#63adf2",
    "#a7cced",
    "#304d6d",
    "#82a0bc",
    "#0a100d",
    "#b9baa3",
    "#d6d5c9",
    "#a22c29",
    "#902923",
    "#260c1a",
    "#432e36",
    "#5f4842",
    "#af8d86",
    "#edbfc6",
    "#29339b",
    "#74a4bc",
    "#b6d6cc",
    "#f1fec6",
    "#ff3a20",
    "#0e131f",
    "#38405f",
    "#59546c",
    "#8b939c",
    "#ff0035",
    "#072ac8",
    "#1e96fc",
    "#a2d6f9",
    "#fcf300",
    "#ffc600",
    "#52489c",
    "#4062bb",
    "#59c3c3",
    "#ebebeb",
    "#f45b69",
    "#0c0f0a",
    "#ff206e",
    "#fbff12",
    "#41ead4",
    "#ffffff",
    "#ff5e5b",
    "#d8d8d8",
    "#ffffea",
    "#00cecb",
    "#ffed66",
    "#336699",
    "#86bbd8",
    "#2f4858",
    "#9ee493",
    "#daf7dc",
    "#3c3744",
    "#090c9b",
    "#3066be",
    "#b4c5e4",
    "#fbfff1",
    "#2364aa",
    "#3da5d9",
    "#73bfb8",
    "#fec601",
    "#ea7317",
    "#abc4ab",
    "#a39171",
    "#dcc9b6",
    "#727d71",
    "#6d4c3d",
    "#faa916",
    "#fbfffe",
    "#6d676e",
    "#1b1b1e",
    "#96031a",
    "#ed6a5a",
    "#f4f1bb",
    "#9bc1bc",
    "#5ca4a9",
    "#e6ebe0",
    "#5603ad",
    "#8367c7",
    "#b3e9c7",
    "#c2f8cb",
    "#f0fff1",
    "#f1dede",
    "#bbacc1",
    "#80727b",
    "#909580",
    "#545643",
    "#d3f8e2",
    "#e4c1f9",
    "#f694c1",
    "#ede7b1",
    "#a9def9",
    "#546a76",
    "#88a0a8",
    "#b4ceb3",
    "#dbd3c9",
    "#fad4d8",
    "#cfdbd5",
    "#e8eddf",
    "#f5cb5c",
    "#242423",
    "#333533",
    "#ecc8af",
    "#e7ad99",
    "#ce796b",
    "#c18c5d",
    "#495867",
    "#b5ca8d",
    "#8bb174",
    "#426b69",
    "#222e50",
    "#2a4849",
    "#f7f052",
    "#f28123",
    "#d34e24",
    "#563f1b",
    "#38726c",
    "#d5c5c8",
    "#9da3a4",
    "#604d53",
    "#db7f8e",
    "#ffdbda",
    "#090c08",
    "#474056",
    "#757083",
    "#8a95a5",
    "#b9c6ae",
    "#00cccc",
    "#00bfb2",
    "#008080",
    "#1ca9c9",
    "#0093af",
    "#638a9f",
    "#f75c03",
    "#563f1b",
    "#a36d90",
    "#b39c4d",
    "#2d00f7",
    "#6a00f4",
    "#8900f2",
    "#a100f2",
    "#b100e8",
    "#ff0a54",
    "#ff477e",
    "#ff5c8a",
    "#ff7096",
    "#ff85a1",
    "#5aa9e6",
    "#7fc8f8",
    "#f9f9f9",
    "#ffe45e",
    "#ff6392",
    "#ff8811",
    "#f4d06f",
    "#fff8f0",
    "#9dd9d2",
    "#392f5a",
    "#05668d",
    "#3e92cc",
    "#fffaff",
    "#d8315b",
    "#1e1b18",
    "#000000",
    "#fffffc",
    "#beb7a4",
    "#ff7f11",
    "#ff3f00",
    "#4d9de0",
    "#e15554",
    "#e1bc29",
    "#3bb273",
    "#7768ae",
    "#880d1e",
    "#dd2d4a",
    "#f26a8d",
    "#f49cbb",
    "#cbeef3",
    "#004e64",
    "#00a5cf",
    "#9fffcb",
    "#25a18e",
    "#7ae582",
    "#8c1c13",
    "#bf4342",
    "#e7d7c1",
    "#a78a7f",
    "#735751",
    "#e06c9f",
    "#f283b6",
    "#edbfb7",
    "#b5bfa1",
    "#6e9887",
    "#ca054d",
    "#3b1c32",
    "#a4d4b4",
    "#ffcf9c",
    "#b96d40",
    "#4f6d7a",
    "#c0d6df",
    "#dbe9ee",
    "#4a6fa5",
    "#166088",
    "#4f6d7a",
    "#c0d6df",
    "#dbe9ee",
    "#4a6fa5",
    "#166088",
    "#888888",
    "#e20074",
    "#c00063",
    "#9e0051",
    "#131314",
    "#a80051",    
    "#f14608",    
    "#47ebff",    
    "#0097a8",        
    "#0e065b",            
]

list_c2 =[
    "#8ecae6",
    "#219ebc",
    "#023047",
    "#ffb703",
    "#fb8500",
    "#606c38",
    "#283618",
    "#fefae0",
    "#dda15e",
    "#bc6c25",
    "#cdb4db",
    "#ffc8dd",
    "#ffafcc",
    "#bde0fe",
    "#a2d2ff",
    "#dad7cd",
    "#a3b18a",
    "#588157",
    "#3a5a40",
    "#344e41",
    "#264653",
    "#2a9d8f",
    "#e9c46a",
    "#f4a261",
    "#e76f51",
    "#ffbe0b",
    "#fb5607",
    "#ff006e",
    "#8338ec",
    "#3a86ff",
    "#780000",
    "#c1121f",
    "#fdf0d5",
    "#003049",
    "#669bbc",
    "#000000",
    "#14213d",
    "#fca311",
    "#e5e5e5",
    "#ffffff",
    "#ffe5ec",
    "#ffc2d1",
    "#ffb3c6",
    "#ff8fab",
    "#fb6f92",
    "#f6bd60",
    "#f7ede2",
    "#f5cac3",
    "#84a59d",
    "#f28482",
    "#fffcf2",
    "#ccc5b9",
    "#403d39",
    "#252422",
    "#eb5e28",
    "#006d77",
    "#83c5be",
    "#edf6f9",
    "#ffddd2",
    "#e29578",
    "#a8d5e2",
    "#f9a620",
    "#ffd449",
    "#548c2f",
    "#104911",
    "#ffd6ff",
    "#e7c6ff",
    "#c8b6ff",
    "#b8c0ff",
    "#bbd0ff",
    "#003049",
    "#d62828",
    "#f77f00",
    "#fcbf49",
    "#eae2b7",
    "#22223b",
    "#4a4e69",
    "#9a8c98",
    "#c9ada7",
    "#f2e9e4",
    "#386641",
    "#6a994e",
    "#a7c957",
    "#f2e8cf",
    "#bc4749",
    "#ff9f1c",
    "#ffbf69",
    "#ffffff",
    "#cbf3f0",
    "#2ec4b6",
    "#ff99c8",
    "#fcf6bd",
    "#d0f4de",
    "#a9def9",
    "#e4c1f9",
    "#22577a",
    "#38a3a5",
    "#57cc99",
    "#80ed99",
    "#c7f9cc",
    "#cad2c5",
    "#84a98c",
    "#52796f",
    "#354f52",
    "#2f3e46",
    "#70d6ff",
    "#ff70a6",
    "#ff9770",
    "#ffd670",
    "#e9ff70",
    "#f72585",
    "#7209b7",
    "#3a0ca3",
    "#4361ee",
    "#4cc9f0",
    "#d00000",
    "#ffba08",
    "#3f88c5",
    "#032b43",
    "#136f63",
    "#0d1b2a",
    "#1b263b",
    "#415a77",
    "#778da9",
    "#e0e1dd",
    "#27187e",
    "#758bfd",
    "#aeb8fe",
    "#f1f2f6",
    "#ff8600",
    "#d8e2dc",
    "#ffe5d9",
    "#ffcad4",
    "#f4acb7",
    "#9d8189",
    "#8cb369",
    "#f4e285",
    "#f4a259",
    "#5b8e7d",
    "#bc4b51",
    "#0081a7",
    "#00afb9",
    "#fdfcdc",
    "#fed9b7",
    "#f07167",
    "#335c67",
    "#fff3b0",
    "#e09f3e",
    "#9e2a2b",
    "#540b0e",
    "#233d4d",
    "#fe7f2d",
    "#fcca46",
    "#a1c181",
    "#619b8a",
    "#008000",
    "#38b000",
    "#70e000",
    "#9ef01a",
    "#ccff33",
    "#2d6a4f",
    "#40916c",
    "#52b788",
    "#74c69d",
    "#95d5b2",
    "#0fa3b1",
    "#b5e2fa",
    "#f9f7f3",
    "#eddea4",
    "#f7a072",
    "#8e9aaf",
    "#cbc0d3",
    "#efd3d7",
    "#feeafa",
    "#dee2ff",
    "#2c6e49",
    "#4c956c",
    "#fefee3",
    "#ffc9b9",
    "#d68c45",
    "#00a6fb",
    "#0582ca",
    "#006494",
    "#003554",
    "#051923",
    "#edafb8",
    "#f7e1d7",
    "#dedbd2",
    "#b0c4b1",
    "#4a5759",
    "#004e64",
    "#00a5cf",
    "#9fffcb",
    "#25a18e",
    "#7ae582",
    "#f9dbbd",
    "#ffa5ab",
    "#da627d",
    "#a53860",
    "#450920",
    "#00916e",
    "#feefe5",
    "#ffcf00",
    "#ee6123",
    "#fa003f",
    "#2e294e",
    "#efbcd5",
    "#be97c6",
    "#8661c1",
    "#4b5267",
    "#820263",
    "#d90368",
    "#eadeda",
    "#2e294e",
    "#ffd400",
    "#355070",
    "#6d597a",
    "#b56576",
    "#e56b6f",
    "#eaac8b",
    "#353535",
    "#3c6e71",
    "#ffffff",
    "#d9d9d9",
    "#284b63",
    "#ffb5a7",
    "#fcd5ce",
    "#f8edeb",
    "#f9dcc4",
    "#fec89a",
    "#227c9d",
    "#17c3b2",
    "#ffcb77",
    "#fef9ef",
    "#fe6d73",
    "#7c6a0a",
    "#babd8d",
    "#ffdac6",
    "#fa9500",
    "#eb6424",
    "#ffe74c",
    "#ff5964",
    "#ffffff",
    "#6bf178",
    "#35a7ff",
    "#780116",
    "#f7b538",
    "#db7c26",
    "#d8572a",
    "#c32f27",
    "#8cb369",
    "#f4e285",
    "#f4a259",
    "#5b8e7d",
    "#bc4b51",
    "#d3f8e2",
    "#e4c1f9",
    "#f694c1",
    "#ede7b1",
    "#a9def9",
    "#d4e09b",
    "#f6f4d2",
    "#cbdfbd",
    "#f19c79",
    "#a44a3f",
    "#f7c59f",
    "#2a324b",
    "#767b91",
    "#c7ccdb",
    "#e1e5ee",
    "#73eedc",
    "#73c2be",
    "#776885",
    "#5f1a37",
    "#04030f",
    "#642ca9",
    "#ff36ab",
    "#ff74d4",
    "#ffb8de",
    "#ffdde1",
    "#2c6e49",
    "#4c956c",
    "#fefee3",
    "#ffc9b9",
    "#d68c45",
    "#d88c9a",
    "#f2d0a9",
    "#f1e3d3",
    "#99c1b9",
    "#8e7dbe",
    "#5465ff",
    "#788bff",
    "#9bb1ff",
    "#bfd7ff",
    "#e2fdff",
    "#2e5266",
    "#6e8898",
    "#9fb1bc",
    "#d3d0cb",
    "#e2c044",  
    "#ccd5ae",
    "#e9edc9",
    "#fefae0",
    "#faedcd",
    "#d4a373",
    "#000814",
    "#001d3d",
    "#003566",
    "#ffc300",
    "#ffd60a",
    "#ffcdb2",
    "#ffb4a2",
    "#e5989b",
    "#b5838d",
    "#6d6875",
    "#edede9",
    "#d6ccc2",
    "#f5ebe0",
    "#e3d5ca",
    "#d5bdaf",
    "#0077b6",
    "#0096c7",
    "#00b4d8",
    "#48cae4",
    "#90e0ef",
    "#132a13",
    "#31572c",
    "#4f772d",
    "#90a955",
    "#ecf39e",
    "#9b5de5",
    "#f15bb5",
    "#fee440",
    "#00bbf9",
    "#00f5d4",
    "#9d0208",
    "#d00000",
    "#dc2f02",
    "#f48c06",
    "#faa307",
    "#001524",
    "#15616d",
    "#ffecd1",
    "#ff7d00",
    "#78290f",
    "#f4f1de",
    "#e07a5f",
    "#3d405b",
    "#81b29a",
    "#f2cc8f",
    "#3d348b",
    "#7678ed",
    "#f7b801",
    "#f18701",
    "#f35b04",
    "#355070",
    "#6d597a",
    "#b56576",
    "#e56b6f",
    "#eaac8b",
    "#463f3a",
    "#8a817c",
    "#bcb8b1",
    "#f4f3ee",
    "#e0afa0",
    "#2b2d42",
    "#8d99ae",
    "#edf2f4",
    "#ef233c",
    "#d90429",
    "#d4e09b",
    "#f6f4d2",
    "#cbdfbd",
    "#f19c79",
    "#a44a3f",
    "#343a40",
    "#495057",
    "#6c757d",
    "#adb5bd",
    "#ced4da",
    "#7f4f24",
    "#936639",
    "#a68a64",
    "#b6ad90",
    "#c2c5aa",
    "#4f000b",
    "#720026",
    "#ce4257",
    "#ff7f51",
    "#ff9b54",
    "#e63946",
    "#f1faee",
    "#a8dadc",
    "#457b9d",
    "#1d3557",
    "#353535",
    "#3c6e71",
    "#ffffff",
    "#d9d9d9",
    "#284b63",
    "#e7ecef",
    "#274c77",
    "#6096ba",
    "#a3cef1",
    "#8b8c89",
    "#6f1d1b",
    "#bb9457",
    "#432818",
    "#99582a",
    "#ffe6a7",
    "#335c67",
    "#fff3b0",
    "#e09f3e",
    "#9e2a2b",
    "#540b0e",
    "#00c3ff",
    "#e84800",
    "#6d0505",
    "#c10f05",
    "#ffef00",
    "#5f0f40",
    "#9a031e",
    "#fb8b24",
    "#e36414",
    "#0f4c5c",
    "#edeec9",
    "#dde7c7",
    "#bfd8bd",
    "#98c9a3",
    "#77bfa3",
    "#800f2f",
    "#a4133c",
    "#c9184a",
    "#ff4d6d",
    "#ff758f",
    "#bee9e8",
    "#62b6cb",
    "#1b4965",
    "#cae9ff",
    "#5fa8d3",
    "#8cb369",
    "#f4e285",
    "#f4a259",
    "#5b8e7d",
    "#bc4b51",
    "#7400b8",
    "#6930c3",
    "#5e60ce",
    "#5390d9",
    "#4ea8de",
    "#0081a7",
    "#00afb9",
    "#fdfcdc",
    "#fed9b7",
    "#f07167",
    "#390099",
    "#9e0059",
    "#ff0054",
    "#ff5400",
    "#ffbd00",
    "#ffffff",
    "#00171f",
    "#003459",
    "#007ea7",
    "#00a8e8",
    "#0a9396",
    "#94d2bd",
    "#e9d8a6",
    "#ee9b00",
    "#ae2012",
    "#cb997e",
    "#ddbea9",
    "#ffe8d6",
    "#b7b7a4",
    "#a5a58d",
    "#95d5b2",
    "#74c69d",
    "#52b788",
    "#40916c",
    "#2d6a4f",
    "#1565c0",
    "#1976d2",
    "#1e88e5",
    "#2196f3",
    "#42a5f5",
    "#231942",
    "#5e548e",
    "#9f86c0",
    "#be95c4",
    "#e0b1cb",
    "#2d7dd2",
    "#97cc04",
    "#eeb902",
    "#f45d01",
    "#474647",
    "#02010a",
    "#04052e",
    "#140152",
    "#22007c",
    "#0d00a4",
    "#c9cba3",
    "#ffe1a8",
    "#e26d5c",
    "#723d46",
    "#472d30",
    "#8ecae6",
    "#219ebc",
    "#023047",
    "#ffc803",
    "#fa0070",
    "#f08080",
    "#f4978e",
    "#f8ad9d",
    "#fbc4ab",
    "#ffdab9",
    "#d8e2dc",
    "#ffffff",
    "#ffcad4",
    "#f4acb7",
    "#9d8189",
    "#080708",
    "#3772ff",
    "#df2935",
    "#fdca40",
    "#e6e8e6",
    "#0b3954",
    "#087e8b",
    "#bfd7ea",
    "#ff5a5f",
    "#c81d25",
    "#ffffff",
    "#84dcc6",
    "#a5ffd6",
    "#ffa69e",
    "#ff686b",
    "#022b3a",
    "#1f7a8c",
    "#bfdbf7",
    "#e1e5f2",
    "#ffffff",
    "#585123",
    "#eec170",
    "#f2a65a",
    "#f58549",
    "#772f1a",
    "#461220",
    "#8c2f39",
    "#b23a48",
    "#fcb9b2",
    "#fed0bb",
    "#5affe7",
    "#08c6ab",
    "#01c38d",
    "#726eff",
    "#132d46",
    "#edae49",
    "#d1495b",
    "#00798c",
    "#30638e",
    "#003d5b",
    "#b9d6f2",
    "#061a40",
    "#0353a4",
    "#006daa",
    "#003559",
    "#031d44",
    "#04395e",
    "#70a288",
    "#dab785",
    "#d5896f",
    "#fbfbf2",
    "#e5e6e4",
    "#cfd2cd",
    "#a6a2a2",
    "#847577",
    "#9c89b8",
    "#f0a6ca",
    "#efc3e6",
    "#f0e6ef",
    "#b8bedd",
    "#06154f",
    "#8a94db",
    "#fcf7e0",
    "#553b72",
    "#e1d9ef",
    "#ff9100",
    "#ff9100",
    "#240046",
    "#3c096c",
    "#5a189a",
    "#f0ead2",
    "#dde5b6",
    "#adc178",
    "#a98467",
    "#6c584c",
    "#03045e",
    "#0077b6",
    "#00b4d8",
    "#90e0ef",
    "#caf0f8",
    "#201e1f",
    "#ff4000",
    "#faaa8d",
    "#feefdd",
    "#50b2c0",
    "#0d3b66",
    "#faf0ca",
    "#f4d35e",
    "#ee964b",
    "#f95738",
    "#001427",
    "#708d81",
    "#f4d58d",
    "#bf0603",
    "#8d0801",
    "#0d1321",
    "#1d2d44",
    "#3e5c76",
    "#748cab",
    "#f0ebd8",
    "#0a1128",
    "#001f54",
    "#034078",
    "#1282a2",
    "#fefcfb",
    "#ede0d4",
    "#e6ccb2",
    "#b08968",
    "#7f5539",
    "#9c6644",
    "#ff7b00",
    "#ff8800",
    "#ff9500",
    "#ffa200",
    "#ffaa00",
    "#642ca9",
    "#ff36ab",
    "#ff74d4",
    "#ffb8de",
    "#ffdde1",
    "#ee6055",
    "#60d394",
    "#aaf683",
    "#ffd97d",
    "#ff9b85",
    "#050505",
    "#1b9aaa",
    "#dddbcb",
    "#f5f1e3",
    "#ffffff",
    "#603808",
    "#6f4518",
    "#8b5e34",
    "#a47148",
    "#d4a276",
    "#f94144",
    "#f9844a",
    "#f9c74f",
    "#90be6d",
    "#277da1",
    "#471ca8",
    "#884ab2",
    "#ff930a",
    "#f24b04",
    "#d1105a",
    "#64113f",
    "#de4d86",
    "#f29ca3",
    "#f7cacd",
    "#84e6f8",
    "#05668d",
    "#028090",
    "#00a896",
    "#02c39a",
    "#f0f3bd",
    "#0a0908",
    "#22333b",
    "#f2f4f3",
    "#a9927d",
    "#5e503f",
    "#9381ff",
    "#b8b8ff",
    "#f8f7ff",
    "#ffeedd",
    "#ffd8be",
    "#7bdff2",
    "#b2f7ef",
    "#eff7f6",
    "#f7d6e0",
    "#f2b5d4",
    "#e6b3b0",
    "#dc94ac",
    "#6b4f99",
    "#3f418b",
    "#162a4f",
    "#00296b",
    "#003f88",
    "#00509d",
    "#fdc500",
    "#ffd500",
    "#fff1e6",
    "#f0efeb",
    "#ddbea9",
    "#a5a58d",
    "#b7b7a4",
    "#90f1ef",
    "#ffd6e0",
    "#ffef9f",
    "#c1fba4",
    "#7bf1a8",
    "#ef476f",
    "#ffd166",
    "#06d6a0",
    "#118ab2",
    "#073b4c",
    "#fcaa67",
    "#b0413e",
    "#ffffc7",
    "#548687",
    "#473335",
    "#f1dac4",
    "#a69cac",
    "#474973",
    "#161b33",
    "#0d0c1d",
    "#083d77",
    "#ebebd3",
    "#f4d35e",
    "#ee964b",
    "#f95738",
    "#73877b",
    "#839788",
    "#bdbbb6",
    "#e5d1d0",
    "#f5e4d7",
    "#813405",
    "#d45113",
    "#f9a03f",
    "#f8dda4",
    "#ddf9c1",
    "#caffbf",
    "#9bf6ff",
    "#a0c4ff",
    "#bdb2ff",
    "#ffc6ff",
    "#ff4800",
    "#ff5400",
    "#ff6000",
    "#ff6d00",
    "#ff7900",
    "#ef6351",
    "#f38375",
    "#f7a399",
    "#fbc3bc",
    "#ffe3e0",
    "#1a535c",
    "#4ecdc4",
    "#f7fff7",
    "#ff6b6b",
    "#ffe66d",
    "#393d3f",
    "#fdfdff",
    "#c6c5b9",
    "#62929e",
    "#546a7b",
    "#ff6b35",
    "#f7c59f",
    "#efefd0",
    "#004e89",
    "#1a659e",
    "#ffd9da",
    "#ea638c",
    "#89023e",
    "#30343f",
    "#1b2021",
    "#fe938c",
    "#e6b89c",
    "#ead2ac",
    "#9cafb7",
    "#4281a4",
    "#01161e",
    "#124559",
    "#598392",
    "#aec3b0",
    "#eff6e0",
    "#3a2e39",
    "#1e555c",
    "#f4d8cd",
    "#edb183",
    "#f15152",
    "#545e75",
    "#63adf2",
    "#a7cced",
    "#304d6d",
    "#82a0bc",
    "#0a100d",
    "#b9baa3",
    "#d6d5c9",
    "#a22c29",
    "#902923",
    "#260c1a",
    "#432e36",
    "#5f4842",
    "#af8d86",
    "#edbfc6",
    "#29339b",
    "#74a4bc",
    "#b6d6cc",
    "#f1fec6",
    "#ff3a20",
    "#0e131f",
    "#38405f",
    "#59546c",
    "#8b939c",
    "#ff0035",
    "#072ac8",
    "#1e96fc",
    "#a2d6f9",
    "#fcf300",
    "#ffc600",
    "#52489c",
    "#4062bb",
    "#59c3c3",
    "#ebebeb",
    "#f45b69",
    "#0c0f0a",
    "#ff206e",
    "#fbff12",
    "#41ead4",
    "#ffffff",
    "#ff5e5b",
    "#d8d8d8",
    "#ffffea",
    "#00cecb",
    "#ffed66",
    "#336699",
    "#86bbd8",
    "#2f4858",
    "#9ee493",
    "#daf7dc",
    "#3c3744",
    "#090c9b",
    "#3066be",
    "#b4c5e4",
    "#fbfff1",
    "#2364aa",
    "#3da5d9",
    "#73bfb8",
    "#fec601",
    "#ea7317",
    "#abc4ab",
    "#a39171",
    "#dcc9b6",
    "#727d71",
    "#6d4c3d",
    "#faa916",
    "#fbfffe",
    "#6d676e",
    "#1b1b1e",
    "#96031a",
    "#ed6a5a",
    "#f4f1bb",
    "#9bc1bc",
    "#5ca4a9",
    "#e6ebe0",
    "#5603ad",
    "#8367c7",
    "#b3e9c7",
    "#c2f8cb",
    "#f0fff1",
    "#f1dede",
    "#bbacc1",
    "#80727b",
    "#909580",
    "#545643",
    "#d3f8e2",
    "#e4c1f9",
    "#f694c1",
    "#ede7b1",
    "#a9def9",
    "#546a76",
    "#88a0a8",
    "#b4ceb3",
    "#dbd3c9",
    "#fad4d8",
    "#cfdbd5",
    "#e8eddf",
    "#f5cb5c",
    "#242423",
    "#333533",
    "#ecc8af",
    "#e7ad99",
    "#ce796b",
    "#c18c5d",
    "#495867",
    "#b5ca8d",
    "#8bb174",
    "#426b69",
    "#222e50",
    "#2a4849",
    "#f7f052",
    "#f28123",
    "#d34e24",
    "#563f1b",
    "#38726c",
    "#d5c5c8",
    "#9da3a4",
    "#604d53",
    "#db7f8e",
    "#ffdbda",
    "#090c08",
    "#474056",
    "#757083",
    "#8a95a5",
    "#b9c6ae",
    "#00cccc",
    "#00bfb2",
    "#008080",
    "#1ca9c9",
    "#0093af",
    "#638a9f",
    "#f75c03",
    "#563f1b",
    "#a36d90",
    "#b39c4d",
    "#2d00f7",
    "#6a00f4",
    "#8900f2",
    "#a100f2",
    "#b100e8",
    "#ff0a54",
    "#ff477e",
    "#ff5c8a",
    "#ff7096",
    "#ff85a1",
    "#5aa9e6",
    "#7fc8f8",
    "#f9f9f9",
    "#ffe45e",
    "#ff6392",
    "#ff8811",
    "#f4d06f",
    "#fff8f0",
    "#9dd9d2",
    "#392f5a",
    "#05668d",
    "#3e92cc",
    "#fffaff",
    "#d8315b",
    "#1e1b18",
    "#000000",
    "#fffffc",
    "#beb7a4",
    "#ff7f11",
    "#ff3f00",
    "#4d9de0",
    "#e15554",
    "#e1bc29",
    "#3bb273",
    "#7768ae",
    "#880d1e",
    "#dd2d4a",
    "#f26a8d",
    "#f49cbb",
    "#cbeef3",
    "#004e64",
    "#00a5cf",
    "#9fffcb",
    "#25a18e",
    "#7ae582",
    "#8c1c13",
    "#bf4342",
    "#e7d7c1",
    "#a78a7f",
    "#735751",
    "#e06c9f",
    "#f283b6",
    "#edbfb7",
    "#b5bfa1",
    "#6e9887",
    "#ca054d",
    "#3b1c32",
    "#a4d4b4",
    "#ffcf9c",
    "#b96d40",
    "#4f6d7a",
    "#c0d6df",
    "#dbe9ee",
    "#4a6fa5",
    "#166088",
    "#4f6d7a",
    "#c0d6df",
    "#dbe9ee",
    "#4a6fa5",
    "#166088",
    "#888888",
    "#e20074",
    "#c00063",
    "#9e0051",
    "#131314",
    "#a80051",    
    "#f14608",    
    "#47ebff",    
    "#0097a8",        
    "#0e065b",            
]

#functions

def fbtnc_1() :
    lbl_new.config(text=list_c[0])
def fbtnc_2() :
    lbl_new.config(text=list_c[1])
def fbtnc_3() :
    lbl_new.config(text=list_c[2])
def fbtnc_4() :
    lbl_new.config(text=list_c[3])
def fbtnc_5() :
    lbl_new.config(text=list_c[4])
def fbtnc_6() :
    lbl_new.config(text=list_c[5])
def fbtnc_7() :
    lbl_new.config(text=list_c[6])
def fbtnc_8() :
    lbl_new.config(text=list_c[7])
def fbtnc_9() :
    lbl_new.config(text=list_c[8])
def fbtnc_10() :
    lbl_new.config(text=list_c[9])
def fbtnc_11() :
    lbl_new.config(text=list_c[10])
def fbtnc_12() :
    lbl_new.config(text=list_c[11])
def fbtnc_13() :
    lbl_new.config(text=list_c[12])
def fbtnc_14() :
    lbl_new.config(text=list_c[13])
def fbtnc_15() :
    lbl_new.config(text=list_c[14])
def fbtnc_16() :
    lbl_new.config(text=list_c[15])
def fbtnc_17() :
    lbl_new.config(text=list_c[16])
def fbtnc_18() :
    lbl_new.config(text=list_c[17])
def fbtnc_19() :
    lbl_new.config(text=list_c[18])
def fbtnc_20() :
    lbl_new.config(text=list_c[19])
def fbtnc_21() :
    lbl_new.config(text=list_c[20])
def fbtnc_22() :
    lbl_new.config(text=list_c[21])
def fbtnc_23() :
    lbl_new.config(text=list_c[22])
def fbtnc_24() :
    lbl_new.config(text=list_c[23])
def fbtnc_25() :
    lbl_new.config(text=list_c[24])
def fbtnc_26() :
    lbl_new.config(text=list_c[25])
def fbtnc_27() :
    lbl_new.config(text=list_c[26])
def fbtnc_28() :
    lbl_new.config(text=list_c[27])
def fbtnc_29() :
    lbl_new.config(text=list_c[28])
def fbtnc_30() :
    lbl_new.config(text=list_c[29])
def fbtnc_31() :
    lbl_new.config(text=list_c[30])
def fbtnc_32() :
    lbl_new.config(text=list_c[31])
def fbtnc_33() :
    lbl_new.config(text=list_c[32])
def fbtnc_34() :
    lbl_new.config(text=list_c[33])
def fbtnc_35() :
    lbl_new.config(text=list_c[34])
def fbtnc_36() :
    lbl_new.config(text=list_c[35])
def fbtnc_37() :
    lbl_new.config(text=list_c[36])
def fbtnc_38() :
    lbl_new.config(text=list_c[37])
def fbtnc_39() :
    lbl_new.config(text=list_c[38])
def fbtnc_40() :
    lbl_new.config(text=list_c[39])
def fbtnc_41() :
    lbl_new.config(text=list_c[40])
def fbtnc_42() :
    lbl_new.config(text=list_c[41])
def fbtnc_43() :
    lbl_new.config(text=list_c[42])
def fbtnc_44() :
    lbl_new.config(text=list_c[43])
def fbtnc_45() :
    lbl_new.config(text=list_c[44])
def fbtnc_46() :
    lbl_new.config(text=list_c[45])
def fbtnc_47() :
    lbl_new.config(text=list_c[46])
def fbtnc_48() :
    lbl_new.config(text=list_c[47])
def fbtnc_49() :
    lbl_new.config(text=list_c[48])
def fbtnc_50() :
    lbl_new.config(text=list_c[49])
def fbtnc_51() :
    lbl_new.config(text=list_c[50])
def fbtnc_52() :
    lbl_new.config(text=list_c[51])
def fbtnc_53() :
    lbl_new.config(text=list_c[52])
def fbtnc_54() :
    lbl_new.config(text=list_c[53])
def fbtnc_55() :
    lbl_new.config(text=list_c[54])
def fbtnc_56() :
    lbl_new.config(text=list_c[55])
def fbtnc_57() :
    lbl_new.config(text=list_c[56])
def fbtnc_58() :
    lbl_new.config(text=list_c[57])
def fbtnc_59() :
    lbl_new.config(text=list_c[58])
def fbtnc_60() :
    lbl_new.config(text=list_c[59])
def fbtnc_61() :
    lbl_new.config(text=list_c[60])
def fbtnc_62() :
    lbl_new.config(text=list_c[61])
def fbtnc_63() :
    lbl_new.config(text=list_c[62])
def fbtnc_64() :
    lbl_new.config(text=list_c[63])
def fbtnc_65() :
    lbl_new.config(text=list_c[64])
def fbtnc_66() :
    lbl_new.config(text=list_c[65])
def fbtnc_67() :
    lbl_new.config(text=list_c[66])
def fbtnc_68() :
    lbl_new.config(text=list_c[67])
def fbtnc_69() :
    lbl_new.config(text=list_c[68])
def fbtnc_70():
    lbl_new.config(text=list_c[69])
def fbtnc_71():
    lbl_new.config(text=list_c[70])
def fbtnc_72() :
    lbl_new.config(text=list_c[71])
def fbtnc_73() :
    lbl_new.config(text=list_c[72])
def fbtnc_74() :
    lbl_new.config(text=list_c[73])
def fbtnc_75() :
    lbl_new.config(text=list_c[74])
def fbtnc_76() :
    lbl_new.config(text=list_c[75])
def fbtnc_77() :
    lbl_new.config(text=list_c[76])
def fbtnc_78() :
    lbl_new.config(text=list_c[77])
def fbtnc_79() :
    lbl_new.config(text=list_c[78])
def fbtnc_80() :
    lbl_new.config(text=list_c[79])
def fbtnc_81() :
    lbl_new.config(text=list_c[80])
def fbtnc_82() :
    lbl_new.config(text=list_c[81])
def fbtnc_83() :
    lbl_new.config(text=list_c[82])
def fbtnc_84() :
    lbl_new.config(text=list_c[83])
def fbtnc_85() :
    lbl_new.config(text=list_c[84])
def fbtnc_86() :
    lbl_new.config(text=list_c[85])
def fbtnc_87() :
    lbl_new.config(text=list_c[86])
def fbtnc_88() :
    lbl_new.config(text=list_c[87])
def fbtnc_89() :
    lbl_new.config(text=list_c[88])
def fbtnc_90() :
    lbl_new.config(text=list_c[89])
def fbtnc_91() :
    lbl_new.config(text=list_c[90])
def fbtnc_92() :
    lbl_new.config(text=list_c[91])
def fbtnc_93() :
    lbl_new.config(text=list_c[92])
def fbtnc_94() :
    lbl_new.config(text=list_c[93])
def fbtnc_95() :
    lbl_new.config(text=list_c[94])
def fbtnc_96() :
    lbl_new.config(text=list_c[95])
def fbtnc_97() :
    lbl_new.config(text=list_c[96])
def fbtnc_98() :
    lbl_new.config(text=list_c[97])
def fbtnc_99() :
    lbl_new.config(text=list_c[98])
def fbtnc_100() :
    lbl_new.config(text=list_c[99])
def fbtnc_101() :
    lbl_new.config(text=list_c[100])
def fbtnc_102() :
    lbl_new.config(text=list_c[101])
def fbtnc_103() :
    lbl_new.config(text=list_c[102])
def fbtnc_104() :
    lbl_new.config(text=list_c[103])
def fbtnc_105() :
    lbl_new.config(text=list_c[104])
def fbtnc_106() :
    lbl_new.config(text=list_c[105])
def fbtnc_107() :
    lbl_new.config(text=list_c[106])
def fbtnc_108() :
    lbl_new.config(text=list_c[107])
def fbtnc_109() :
    lbl_new.config(text=list_c[108])
def fbtnc_110() :
    lbl_new.config(text=list_c[109])
def fbtnc_111() :
    lbl_new.config(text=list_c[110])
def fbtnc_112() :
    lbl_new.config(text=list_c[111])
def fbtnc_113() :
    lbl_new.config(text=list_c[112])
def fbtnc_114() :
    lbl_new.config(text=list_c[113])
def fbtnc_115() :
    lbl_new.config(text=list_c[114])
def fbtnc_116() :
    lbl_new.config(text=list_c[115])
def fbtnc_117() :
    lbl_new.config(text=list_c[116])
def fbtnc_118() :
    lbl_new.config(text=list_c[117])
def fbtnc_119() :
    lbl_new.config(text=list_c[118])
def fbtnc_120() :
    lbl_new.config(text=list_c[119])
def fbtnc_121() :
    lbl_new.config(text=list_c[120])
def fbtnc_122() :
    lbl_new.config(text=list_c[121])
def fbtnc_123() :
    lbl_new.config(text=list_c[122])
def fbtnc_124() :
    lbl_new.config(text=list_c[123])
def fbtnc_125() :
    lbl_new.config(text=list_c[124])
def fbtnc_126() :
    lbl_new.config(text=list_c[125])
def fbtnc_127() :
    lbl_new.config(text=list_c[126])
def fbtnc_128() :
    lbl_new.config(text=list_c[127])
def fbtnc_129() :
    lbl_new.config(text=list_c[128])
def fbtnc_130() :
    lbl_new.config(text=list_c[129])
def fbtnc_131() :
    lbl_new.config(text=list_c[130])
def fbtnc_132() :
    lbl_new.config(text=list_c[131])
def fbtnc_133() :
    lbl_new.config(text=list_c[132])
def fbtnc_134() :
    lbl_new.config(text=list_c[133])
def fbtnc_135() :
    lbl_new.config(text=list_c[134])
def fbtnc_136() :
    lbl_new.config(text=list_c[135])
def fbtnc_137() :
    lbl_new.config(text=list_c[136])
def fbtnc_138() :
    lbl_new.config(text=list_c[137])
def fbtnc_139() :
    lbl_new.config(text=list_c[138])
def fbtnc_140() :
    lbl_new.config(text=list_c[139])
def fbtnc_141() :
    lbl_new.config(text=list_c[140])
def fbtnc_142() :
    lbl_new.config(text=list_c[141])
def fbtnc_143() :
    lbl_new.config(text=list_c[142])
def fbtnc_144() :
    lbl_new.config(text=list_c[143])
def fbtnc_145() :
    lbl_new.config(text=list_c[144])
def fbtnc_146() :
    lbl_new.config(text=list_c[145])
def fbtnc_147() :
    lbl_new.config(text=list_c[146])
def fbtnc_148() :
    lbl_new.config(text=list_c[147])
def fbtnc_149() :
    lbl_new.config(text=list_c[148])
def fbtnc_150() :
    lbl_new.config(text=list_c[149])
def fbtnc_151() :
    lbl_new.config(text=list_c[150])
def fbtnc_152() :
    lbl_new.config(text=list_c[151])
def fbtnc_153() :
    lbl_new.config(text=list_c[152])
def fbtnc_154() :
    lbl_new.config(text=list_c[153])
def fbtnc_155() :
    lbl_new.config(text=list_c[154])
def fbtnc_156() :
    lbl_new.config(text=list_c[155])
def fbtnc_157() :
    lbl_new.config(text=list_c[156])
def fbtnc_158() :
    lbl_new.config(text=list_c[157])
def fbtnc_159() :
    lbl_new.config(text=list_c[158])
def fbtnc_160() :
    lbl_new.config(text=list_c[159])
def fbtnc_161() :
    lbl_new.config(text=list_c[160])
def fbtnc_162() :
    lbl_new.config(text=list_c[161])
def fbtnc_163() :
    lbl_new.config(text=list_c[162])
def fbtnc_164() :
    lbl_new.config(text=list_c[163])
def fbtnc_165() :
    lbl_new.config(text=list_c[164])
def fbtnc_166() :
    lbl_new.config(text=list_c[165])
def fbtnc_167() :
    lbl_new.config(text=list_c[166])
def fbtnc_168() :
    lbl_new.config(text=list_c[167])
def fbtnc_169() :
    lbl_new.config(text=list_c[168])
def fbtnc_170() :
    lbl_new.config(text=list_c[169])
def fbtnc_171() :
    lbl_new.config(text=list_c[170])
def fbtnc_172() :
    lbl_new.config(text=list_c[171])
def fbtnc_173() :
    lbl_new.config(text=list_c[172])
def fbtnc_174() :
    lbl_new.config(text=list_c[173])
def fbtnc_175() :
    lbl_new.config(text=list_c[174])
def fbtnc_176() :
    lbl_new.config(text=list_c[175])
def fbtnc_177() :
    lbl_new.config(text=list_c[176])
def fbtnc_178() :
    lbl_new.config(text=list_c[177])
def fbtnc_179() :
    lbl_new.config(text=list_c[178])
def fbtnc_180() :
    lbl_new.config(text=list_c[179])
def fbtnc_181() :
    lbl_new.config(text=list_c[180])
def fbtnc_182() :
    lbl_new.config(text=list_c[181])
def fbtnc_183() :
    lbl_new.config(text=list_c[182])
def fbtnc_184() :
    lbl_new.config(text=list_c[183])
def fbtnc_185() :
    lbl_new.config(text=list_c[184])
def fbtnc_186() :
    lbl_new.config(text=list_c[185])
def fbtnc_187() :
    lbl_new.config(text=list_c[186])
def fbtnc_188() :
    lbl_new.config(text=list_c[187])
def fbtnc_189() :
    lbl_new.config(text=list_c[188])
def fbtnc_190() :
    lbl_new.config(text=list_c[189])
def fbtnc_191() :
    lbl_new.config(text=list_c[190])
def fbtnc_192() :
    lbl_new.config(text=list_c[191])
def fbtnc_193() :
    lbl_new.config(text=list_c[192])
def fbtnc_194() :
    lbl_new.config(text=list_c[193])
def fbtnc_195() :
    lbl_new.config(text=list_c[194])
def fbtnc_196() :
    lbl_new.config(text=list_c[195])
def fbtnc_197() :
    lbl_new.config(text=list_c[196])
def fbtnc_198() :
    lbl_new.config(text=list_c[197])
def fbtnc_199() :
    lbl_new.config(text=list_c[198])
def fbtnc_200() :
    lbl_new.config(text=list_c[199])
def fbtnc_201() :
    lbl_new.config(text=list_c[200])
def fbtnc_202() :
    lbl_new.config(text=list_c[201])
def fbtnc_203() :
    lbl_new.config(text=list_c[202])
def fbtnc_204() :
    lbl_new.config(text=list_c[203])
def fbtnc_205() :
    lbl_new.config(text=list_c[204])
def fbtnc_206() :
    lbl_new.config(text=list_c[205])
def fbtnc_207() :
    lbl_new.config(text=list_c[206])
def fbtnc_208() :
    lbl_new.config(text=list_c[207])
def fbtnc_209() :
    lbl_new.config(text=list_c[208])
def fbtnc_210() :
    lbl_new.config(text=list_c[209])
def fbtnc_211() :
    lbl_new.config(text=list_c[210])
def fbtnc_212() :
    lbl_new.config(text=list_c[211])
def fbtnc_213() :
    lbl_new.config(text=list_c[212])
def fbtnc_214() :
    lbl_new.config(text=list_c[213])
def fbtnc_215() :
    lbl_new.config(text=list_c[214])
def fbtnc_216() :
    lbl_new.config(text=list_c[215])
def fbtnc_217() :
    lbl_new.config(text=list_c[216])
def fbtnc_218() :
    lbl_new.config(text=list_c[217])
def fbtnc_219() :
    lbl_new.config(text=list_c[218])
def fbtnc_220() :
    lbl_new.config(text=list_c[219])
def fbtnc_221() :
    lbl_new.config(text=list_c[220])
def fbtnc_222() :
    lbl_new.config(text=list_c[221])
def fbtnc_223() :
    lbl_new.config(text=list_c[222])
def fbtnc_224() :
    lbl_new.config(text=list_c[223])
def fbtnc_225() :
    lbl_new.config(text=list_c[224])
def fbtnc_226() :
    lbl_new.config(text=list_c[225])
def fbtnc_227() :
    lbl_new.config(text=list_c[226])
def fbtnc_228() :
    lbl_new.config(text=list_c[227])
def fbtnc_229() :
    lbl_new.config(text=list_c[228])
def fbtnc_230() :
    lbl_new.config(text=list_c[229])
def fbtnc_231() :
    lbl_new.config(text=list_c[230])
def fbtnc_232() :
    lbl_new.config(text=list_c[231])
def fbtnc_233() :
    lbl_new.config(text=list_c[232])
def fbtnc_234() :
    lbl_new.config(text=list_c[233])
def fbtnc_235() :
    lbl_new.config(text=list_c[234])
def fbtnc_236() :
    lbl_new.config(text=list_c[235])
def fbtnc_237() :
    lbl_new.config(text=list_c[236])
def fbtnc_238() :
    lbl_new.config(text=list_c[237])
def fbtnc_239() :
    lbl_new.config(text=list_c[238])
def fbtnc_240() :
    lbl_new.config(text=list_c[239])
def fbtnc_241() :
    lbl_new.config(text=list_c[240])
def fbtnc_242() :
    lbl_new.config(text=list_c[241])
def fbtnc_243() :
    lbl_new.config(text=list_c[242])
def fbtnc_244() :
    lbl_new.config(text=list_c[243])
def fbtnc_245() :
    lbl_new.config(text=list_c[244])
def fbtnc_246() :
    lbl_new.config(text=list_c[245])
def fbtnc_247() :
    lbl_new.config(text=list_c[246])
def fbtnc_248() :
    lbl_new.config(text=list_c[247])
def fbtnc_249() :
    lbl_new.config(text=list_c[248])
def fbtnc_250() :
    lbl_new.config(text=list_c[249])
def fbtnc_251() :
    lbl_new.config(text=list_c[250])
def fbtnc_252() :
    lbl_new.config(text=list_c[251])
def fbtnc_253() :
    lbl_new.config(text=list_c[252])
def fbtnc_254() :
    lbl_new.config(text=list_c[253])
def fbtnc_255() :
    lbl_new.config(text=list_c[254])
def fbtnc_256() :
    lbl_new.config(text=list_c[255])
def fbtnc_257() :
    lbl_new.config(text=list_c[256])
def fbtnc_258() :
    lbl_new.config(text=list_c[257])
def fbtnc_259() :
    lbl_new.config(text=list_c[258])
def fbtnc_260() :
    lbl_new.config(text=list_c[259])
def fbtnc_261() :
    lbl_new.config(text=list_c[260])
def fbtnc_262() :
    lbl_new.config(text=list_c[261])
def fbtnc_263() :
    lbl_new.config(text=list_c[262])
def fbtnc_264() :
    lbl_new.config(text=list_c[263])
def fbtnc_265() :
    lbl_new.config(text=list_c[264])
def fbtnc_266() :
    lbl_new.config(text=list_c[265])
def fbtnc_267() :
    lbl_new.config(text=list_c[266])
def fbtnc_268() :
    lbl_new.config(text=list_c[267])
def fbtnc_269() :
    lbl_new.config(text=list_c[268])
def fbtnc_270() :
    lbl_new.config(text=list_c[269])
def fbtnc_271() :
    lbl_new.config(text=list_c[270])
def fbtnc_272() :
    lbl_new.config(text=list_c[271])
def fbtnc_273() :
    lbl_new.config(text=list_c[272])
def fbtnc_274() :
    lbl_new.config(text=list_c[273])
def fbtnc_275() :
    lbl_new.config(text=list_c[274])
def fbtnc_276() :
    lbl_new.config(text=list_c[275])
def fbtnc_277() :
    lbl_new.config(text=list_c[276])
def fbtnc_278() :
    lbl_new.config(text=list_c[277])
def fbtnc_279() :
    lbl_new.config(text=list_c[278])
def fbtnc_280() :
    lbl_new.config(text=list_c[279])
def fbtnc_281() :
    lbl_new.config(text=list_c[280])
def fbtnc_282() :
    lbl_new.config(text=list_c[281])
def fbtnc_283() :
    lbl_new.config(text=list_c[282])
def fbtnc_284() :
    lbl_new.config(text=list_c[283])
def fbtnc_285() :
    lbl_new.config(text=list_c[284])
def fbtnc_286() :
    lbl_new.config(text=list_c[285])
def fbtnc_287() :
    lbl_new.config(text=list_c[286])
def fbtnc_288() :
    lbl_new.config(text=list_c[287])
def fbtnc_289() :
    lbl_new.config(text=list_c[288])
def fbtnc_290() :
    lbl_new.config(text=list_c[289])
def fbtnc_291() :
    lbl_new.config(text=list_c[290])
def fbtnc_292() :
    lbl_new.config(text=list_c[291])
def fbtnc_293() :
    lbl_new.config(text=list_c[292])
def fbtnc_294() :
    lbl_new.config(text=list_c[293])
def fbtnc_295() :
    lbl_new.config(text=list_c[294])
def fbtnc_296() :
    lbl_new.config(text=list_c[295])
def fbtnc_297() :
    lbl_new.config(text=list_c[296])
def fbtnc_298() :
    lbl_new.config(text=list_c[297])
def fbtnc_299() :
    lbl_new.config(text=list_c[298])
def fbtnc_300() :
    lbl_new.config(text=list_c[299])
def fbtnc_301() :
    lbl_new.config(text=list_c[300])
def fbtnc_302() :
    lbl_new.config(text=list_c[301])
def fbtnc_303() :
    lbl_new.config(text=list_c[302])
def fbtnc_304() :
    lbl_new.config(text=list_c[303])
def fbtnc_305() :
    lbl_new.config(text=list_c[304])
def fbtnc_306() :
    lbl_new.config(text=list_c[305])
def fbtnc_307() :
    lbl_new.config(text=list_c[306])
def fbtnc_308() :
    lbl_new.config(text=list_c[307])
def fbtnc_309() :
    lbl_new.config(text=list_c[308])
def fbtnc_310() :
    lbl_new.config(text=list_c[309])
def fbtnc_311() :
    lbl_new.config(text=list_c[310])
def fbtnc_312() :
    lbl_new.config(text=list_c[311])
def fbtnc_313() :
    lbl_new.config(text=list_c[312])
def fbtnc_314() :
    lbl_new.config(text=list_c[313])
def fbtnc_315() :
    lbl_new.config(text=list_c[314])
def fbtnc_316() :
    lbl_new.config(text=list_c[315])
def fbtnc_317() :
    lbl_new.config(text=list_c[316])
def fbtnc_318() :
    lbl_new.config(text=list_c[317])
def fbtnc_319() :
    lbl_new.config(text=list_c[318])
def fbtnc_320() :
    lbl_new.config(text=list_c[319])
def fbtnc_321() :
    lbl_new.config(text=list_c[320])
def fbtnc_322() :
    lbl_new.config(text=list_c[321])
def fbtnc_323() :
    lbl_new.config(text=list_c[322])
def fbtnc_324() :
    lbl_new.config(text=list_c[323])
def fbtnc_325() :
    lbl_new.config(text=list_c[324])
def fbtnc_326() :
    lbl_new.config(text=list_c[325])
def fbtnc_327() :
    lbl_new.config(text=list_c[326])
def fbtnc_328() :
    lbl_new.config(text=list_c[327])
def fbtnc_329() :
    lbl_new.config(text=list_c[328])
def fbtnc_330() :
    lbl_new.config(text=list_c[329])
def fbtnc_331() :
    lbl_new.config(text=list_c[330])
def fbtnc_332() :
    lbl_new.config(text=list_c[331])
def fbtnc_333() :
    lbl_new.config(text=list_c[332])
def fbtnc_334() :
    lbl_new.config(text=list_c[333])
def fbtnc_335() :
    lbl_new.config(text=list_c[334])
def fbtnc_336() :
    lbl_new.config(text=list_c[335])
def fbtnc_337() :
    lbl_new.config(text=list_c[336])
def fbtnc_338() :
    lbl_new.config(text=list_c[337])
def fbtnc_339() :
    lbl_new.config(text=list_c[338])
def fbtnc_340() :
    lbl_new.config(text=list_c[339])
def fbtnc_341() :
    lbl_new.config(text=list_c[340])
def fbtnc_342() :
    lbl_new.config(text=list_c[341])
def fbtnc_343() :
    lbl_new.config(text=list_c[342])
def fbtnc_344() :
    lbl_new.config(text=list_c[343])
def fbtnc_345() :
    lbl_new.config(text=list_c[344])
def fbtnc_346() :
    lbl_new.config(text=list_c[345])
def fbtnc_347() :
    lbl_new.config(text=list_c[346])
def fbtnc_348() :
    lbl_new.config(text=list_c[347])
def fbtnc_349() :
    lbl_new.config(text=list_c[348])
def fbtnc_350() :
    lbl_new.config(text=list_c[349])
def fbtnc_351() :
    lbl_new.config(text=list_c[350])
def fbtnc_352() :
    lbl_new.config(text=list_c[351])
def fbtnc_353() :
    lbl_new.config(text=list_c[352])
def fbtnc_354() :
    lbl_new.config(text=list_c[353])
def fbtnc_355() :
    lbl_new.config(text=list_c[354])
def fbtnc_356() :
    lbl_new.config(text=list_c[355])
def fbtnc_357() :
    lbl_new.config(text=list_c[356])
def fbtnc_358() :
    lbl_new.config(text=list_c[357])
def fbtnc_359() :
    lbl_new.config(text=list_c[358])
def fbtnc_360() :
    lbl_new.config(text=list_c[359])
def fbtnc_361() :
    lbl_new.config(text=list_c[360])
def fbtnc_362() :
    lbl_new.config(text=list_c[361])
def fbtnc_363() :
    lbl_new.config(text=list_c[362])
def fbtnc_364() :
    lbl_new.config(text=list_c[363])
def fbtnc_365() :
    lbl_new.config(text=list_c[364])
def fbtnc_366() :
    lbl_new.config(text=list_c[365])
def fbtnc_367() :
    lbl_new.config(text=list_c[366])
def fbtnc_368() :
    lbl_new.config(text=list_c[367])
def fbtnc_369() :
    lbl_new.config(text=list_c[368])
def fbtnc_370() :
    lbl_new.config(text=list_c[369])
def fbtnc_371() :
    lbl_new.config(text=list_c[370])
def fbtnc_372() :
    lbl_new.config(text=list_c[371])
def fbtnc_373() :
    lbl_new.config(text=list_c[372])
def fbtnc_374() :
    lbl_new.config(text=list_c[373])
def fbtnc_375() :
    lbl_new.config(text=list_c[374])
def fbtnc_376() :
    lbl_new.config(text=list_c[375])
def fbtnc_377() :
    lbl_new.config(text=list_c[376])
def fbtnc_378() :
    lbl_new.config(text=list_c[377])
def fbtnc_379() :
    lbl_new.config(text=list_c[378])
def fbtnc_380() :
    lbl_new.config(text=list_c[379])
def fbtnc_381() :
    lbl_new.config(text=list_c[380])
def fbtnc_382() :
    lbl_new.config(text=list_c[381])
def fbtnc_383() :
    lbl_new.config(text=list_c[382])
def fbtnc_384() :
    lbl_new.config(text=list_c[383])
def fbtnc_385() :
    lbl_new.config(text=list_c[384])
def fbtnc_386() :
    lbl_new.config(text=list_c[385])
def fbtnc_387() :
    lbl_new.config(text=list_c[386])
def fbtnc_388() :
    lbl_new.config(text=list_c[387])
def fbtnc_389() :
    lbl_new.config(text=list_c[388])
def fbtnc_390() :
    lbl_new.config(text=list_c[389])
def fbtnc_391() :
    lbl_new.config(text=list_c[390])
def fbtnc_392() :
    lbl_new.config(text=list_c[391])
def fbtnc_393() :
    lbl_new.config(text=list_c[392])
def fbtnc_394() :
    lbl_new.config(text=list_c[393])
def fbtnc_395() :
    lbl_new.config(text=list_c[394])
def fbtnc_396() :
    lbl_new.config(text=list_c[395])
def fbtnc_397() :
    lbl_new.config(text=list_c[396])
def fbtnc_398() :
    lbl_new.config(text=list_c[397])
def fbtnc_399() :
    lbl_new.config(text=list_c[398])
def fbtnc_400() :
    lbl_new.config(text=list_c[399])
def fbtnc_401() :
    lbl_new.config(text=list_c[400])
def fbtnc_402():
    lbl_new.config(text=list_c[401])
def fbtnc_403():
    lbl_new.config(text=list_c[402])
def fbtnc_404():
    lbl_new.config(text=list_c[403])
def fbtnc_405():
    lbl_new.config(text=list_c[404])
def fbtnc_406():
    lbl_new.config(text=list_c[405])
def fbtnc_407():
    lbl_new.config(text=list_c[406])
def fbtnc_408():
    lbl_new.config(text=list_c[407])
def fbtnc_409():
    lbl_new.config(text=list_c[408])
def fbtnc_410():
    lbl_new.config(text=list_c[409])
def fbtnc_411():
    lbl_new.config(text=list_c[410])
def fbtnc_412():
    lbl_new.config(text=list_c[411])
def fbtnc_413():
    lbl_new.config(text=list_c[412])
def fbtnc_414():
    lbl_new.config(text=list_c[413])
def fbtnc_415():
    lbl_new.config(text=list_c[414])
def fbtnc_416():
    lbl_new.config(text=list_c[415])
def fbtnc_417():
    lbl_new.config(text=list_c[416])
def fbtnc_418():
    lbl_new.config(text=list_c[417])
def fbtnc_419():
    lbl_new.config(text=list_c[418])
def fbtnc_420():
    lbl_new.config(text=list_c[419])
def fbtnc_421():
    lbl_new.config(text=list_c[420])
def fbtnc_422():
    lbl_new.config(text=list_c[421])
def fbtnc_423():
    lbl_new.config(text=list_c[422])
def fbtnc_424():
    lbl_new.config(text=list_c[423])
def fbtnc_425():
    lbl_new.config(text=list_c[424])
def fbtnc_426():
    lbl_new.config(text=list_c[425])
def fbtnc_427():
    lbl_new.config(text=list_c[426])
def fbtnc_428():
    lbl_new.config(text=list_c[427])
def fbtnc_429():
    lbl_new.config(text=list_c[428])
def fbtnc_430():
    lbl_new.config(text=list_c[429])
def fbtnc_431():
    lbl_new.config(text=list_c[430])
def fbtnc_432():
    lbl_new.config(text=list_c[431])
def fbtnc_433():
    lbl_new.config(text=list_c[432])
def fbtnc_434():
    lbl_new.config(text=list_c[433])
def fbtnc_435():
    lbl_new.config(text=list_c[434])
def fbtnc_436():
    lbl_new.config(text=list_c[435])
def fbtnc_437():
    lbl_new.config(text=list_c[436])
def fbtnc_438():
    lbl_new.config(text=list_c[437])
def fbtnc_439():
    lbl_new.config(text=list_c[438])
def fbtnc_440():
    lbl_new.config(text=list_c[439])
def fbtnc_441():
    lbl_new.config(text=list_c[440])
def fbtnc_442():
    lbl_new.config(text=list_c[441])
def fbtnc_443():
    lbl_new.config(text=list_c[442])
def fbtnc_444():
    lbl_new.config(text=list_c[443])
def fbtnc_445():
    lbl_new.config(text=list_c[444])
def fbtnc_446():
    lbl_new.config(text=list_c[445])
def fbtnc_447():
    lbl_new.config(text=list_c[446])
def fbtnc_448():
    lbl_new.config(text=list_c[447])
def fbtnc_449():
    lbl_new.config(text=list_c[448])
def fbtnc_450():
    lbl_new.config(text=list_c[449])
def fbtnc_451():
    lbl_new.config(text=list_c[450])
def fbtnc_452():
    lbl_new.config(text=list_c[451])
def fbtnc_453():
    lbl_new.config(text=list_c[452])
def fbtnc_454():
    lbl_new.config(text=list_c[453])
def fbtnc_455():
    lbl_new.config(text=list_c[454])
def fbtnc_456():
    lbl_new.config(text=list_c[455])
def fbtnc_457():
    lbl_new.config(text=list_c[456])
def fbtnc_458():
    lbl_new.config(text=list_c[457])
def fbtnc_459():
    lbl_new.config(text=list_c[458])
def fbtnc_460():
    lbl_new.config(text=list_c[459])
def fbtnc_461():
    lbl_new.config(text=list_c[460])
def fbtnc_462():
    lbl_new.config(text=list_c[461])
def fbtnc_463():
    lbl_new.config(text=list_c[462])
def fbtnc_464():
    lbl_new.config(text=list_c[463])
def fbtnc_465():
    lbl_new.config(text=list_c[464])
def fbtnc_466():
    lbl_new.config(text=list_c[465])
def fbtnc_467():
    lbl_new.config(text=list_c[466])
def fbtnc_468():
    lbl_new.config(text=list_c[467])
def fbtnc_469():
    lbl_new.config(text=list_c[468])
def fbtnc_470():
    lbl_new.config(text=list_c[469])
def fbtnc_471():
    lbl_new.config(text=list_c[470])
def fbtnc_472():
    lbl_new.config(text=list_c[471])
def fbtnc_473():
    lbl_new.config(text=list_c[472])
def fbtnc_474():
    lbl_new.config(text=list_c[473])
def fbtnc_475():
    lbl_new.config(text=list_c[474])
def fbtnc_476():
    lbl_new.config(text=list_c[475])
def fbtnc_477():
    lbl_new.config(text=list_c[476])
def fbtnc_478():
    lbl_new.config(text=list_c[477])
def fbtnc_479():
    lbl_new.config(text=list_c[478])
def fbtnc_480():
    lbl_new.config(text=list_c[479])
def fbtnc_481():
    lbl_new.config(text=list_c[480])
def fbtnc_482():
    lbl_new.config(text=list_c[481])
def fbtnc_483():
    lbl_new.config(text=list_c[482])
def fbtnc_484():
    lbl_new.config(text=list_c[483])
def fbtnc_485():
    lbl_new.config(text=list_c[484])
def fbtnc_486():
    lbl_new.config(text=list_c[485])
def fbtnc_487():
    lbl_new.config(text=list_c[486])
def fbtnc_488():
    lbl_new.config(text=list_c[487])
def fbtnc_489():
    lbl_new.config(text=list_c[488])
def fbtnc_490():
    lbl_new.config(text=list_c[489])
def fbtnc_491():
    lbl_new.config(text=list_c[490])
def fbtnc_492():
    lbl_new.config(text=list_c[491])
def fbtnc_493():
    lbl_new.config(text=list_c[492])
def fbtnc_494():
    lbl_new.config(text=list_c[493])
def fbtnc_495():
    lbl_new.config(text=list_c[494])
def fbtnc_496():
    lbl_new.config(text=list_c[495])
def fbtnc_497():
    lbl_new.config(text=list_c[496])
def fbtnc_498():
    lbl_new.config(text=list_c[497])
def fbtnc_499():
    lbl_new.config(text=list_c[498])
def fbtnc_500():
    lbl_new.config(text=list_c[499])
def fbtnc_501():
    lbl_new.config(text=list_c[500])
def fbtnc_502():
    lbl_new.config(text=list_c[501])
def fbtnc_503():
    lbl_new.config(text=list_c[502])
def fbtnc_504():
    lbl_new.config(text=list_c[503])
def fbtnc_505():
    lbl_new.config(text=list_c[504])
def fbtnc_506():
    lbl_new.config(text=list_c[505])
def fbtnc_507():
    lbl_new.config(text=list_c[506])
def fbtnc_508():
    lbl_new.config(text=list_c[507])
def fbtnc_509():
    lbl_new.config(text=list_c[508])
def fbtnc_510():
    lbl_new.config(text=list_c[509])
def fbtnc_511():
    lbl_new.config(text=list_c[510])
def fbtnc_512():
    lbl_new.config(text=list_c[511])
def fbtnc_513():
    lbl_new.config(text=list_c[512])
def fbtnc_514():
    lbl_new.config(text=list_c[513])
def fbtnc_515():
    lbl_new.config(text=list_c[514])
def fbtnc_516():
    lbl_new.config(text=list_c[515])
def fbtnc_517():
    lbl_new.config(text=list_c[516])
def fbtnc_518():
    lbl_new.config(text=list_c[517])
def fbtnc_519():
    lbl_new.config(text=list_c[518])
def fbtnc_520():
    lbl_new.config(text=list_c[519])
def fbtnc_521():
    lbl_new.config(text=list_c[520])
def fbtnc_522():
    lbl_new.config(text=list_c[521])
def fbtnc_523():
    lbl_new.config(text=list_c[522])
def fbtnc_524():
    lbl_new.config(text=list_c[523])
def fbtnc_525():
    lbl_new.config(text=list_c[524])
def fbtnc_526():
    lbl_new.config(text=list_c[525])
def fbtnc_527():
    lbl_new.config(text=list_c[526])
def fbtnc_528():
    lbl_new.config(text=list_c[527])
def fbtnc_529():
    lbl_new.config(text=list_c[528])
def fbtnc_530():
    lbl_new.config(text=list_c[529])
def fbtnc_531():
    lbl_new.config(text=list_c[530])
def fbtnc_532():
    lbl_new.config(text=list_c[531])
def fbtnc_533():
    lbl_new.config(text=list_c[532])
def fbtnc_534():
    lbl_new.config(text=list_c[533])
def fbtnc_535():
    lbl_new.config(text=list_c[534])
def fbtnc_536():
    lbl_new.config(text=list_c[535])
def fbtnc_537():
    lbl_new.config(text=list_c[536])
def fbtnc_538():
    lbl_new.config(text=list_c[537])
def fbtnc_539():
    lbl_new.config(text=list_c[538])
def fbtnc_540():
    lbl_new.config(text=list_c[539])
def fbtnc_541():
    lbl_new.config(text=list_c[540])
def fbtnc_542():
    lbl_new.config(text=list_c[541])
def fbtnc_543():
    lbl_new.config(text=list_c[542])
def fbtnc_544():
    lbl_new.config(text=list_c[543])
def fbtnc_545():
    lbl_new.config(text=list_c[544])
def fbtnc_546():
    lbl_new.config(text=list_c[545])
def fbtnc_547():
    lbl_new.config(text=list_c[546])
def fbtnc_548():
    lbl_new.config(text=list_c[547])
def fbtnc_549():
    lbl_new.config(text=list_c[548])
def fbtnc_550():
    lbl_new.config(text=list_c[549])
def fbtnc_551():
    lbl_new.config(text=list_c[550])
def fbtnc_552():
    lbl_new.config(text=list_c[551])
def fbtnc_553():
    lbl_new.config(text=list_c[552])
def fbtnc_554():
    lbl_new.config(text=list_c[553])
def fbtnc_555():
    lbl_new.config(text=list_c[554])
def fbtnc_556():
    lbl_new.config(text=list_c[555])
def fbtnc_557():
    lbl_new.config(text=list_c[556])
def fbtnc_558():
    lbl_new.config(text=list_c[557])
def fbtnc_559():
    lbl_new.config(text=list_c[558])
def fbtnc_560():
    lbl_new.config(text=list_c[559])
def fbtnc_561():
    lbl_new.config(text=list_c[560])
def fbtnc_562():
    lbl_new.config(text=list_c[561])
def fbtnc_563():
    lbl_new.config(text=list_c[562])
def fbtnc_564():
    lbl_new.config(text=list_c[563])
def fbtnc_565():
    lbl_new.config(text=list_c[564])
def fbtnc_566():
    lbl_new.config(text=list_c[565])
def fbtnc_567():
    lbl_new.config(text=list_c[566])
def fbtnc_568():
    lbl_new.config(text=list_c[567])
def fbtnc_569():
    lbl_new.config(text=list_c[568])
def fbtnc_570():
    lbl_new.config(text=list_c[569])
def fbtnc_571() :
    lbl_new.config(text=list_c[570])
def fbtnc_572():
    lbl_new.config(text=list_c[571])
def fbtnc_573():
    lbl_new.config(text=list_c[572])
def fbtnc_574():
    lbl_new.config(text=list_c[573])
def fbtnc_575():
    lbl_new.config(text=list_c[574])
def fbtnc_576():
    lbl_new.config(text=list_c[575])
def fbtnc_577():
    lbl_new.config(text=list_c[576])
def fbtnc_578():
    lbl_new.config(text=list_c[577])
def fbtnc_579():
    lbl_new.config(text=list_c[578])
def fbtnc_580():
    lbl_new.config(text=list_c[579])
def fbtnc_581():
    lbl_new.config(text=list_c[580])
def fbtnc_582():
    lbl_new.config(text=list_c[581])
def fbtnc_583():
    lbl_new.config(text=list_c[582])
def fbtnc_584():
    lbl_new.config(text=list_c[583])
def fbtnc_585():
    lbl_new.config(text=list_c[584])
def fbtnc_586():
    lbl_new.config(text=list_c[585])
def fbtnc_587():
    lbl_new.config(text=list_c[586])
def fbtnc_588():
    lbl_new.config(text=list_c[587])
def fbtnc_589():
    lbl_new.config(text=list_c[588])
def fbtnc_590():
    lbl_new.config(text=list_c[589])
def fbtnc_591():
    lbl_new.config(text=list_c[590])
def fbtnc_592():
    lbl_new.config(text=list_c[591])
def fbtnc_593():
    lbl_new.config(text=list_c[592])
def fbtnc_594():
    lbl_new.config(text=list_c[593])
def fbtnc_595():
    lbl_new.config(text=list_c[594])
def fbtnc_596():
    lbl_new.config(text=list_c[595])
def fbtnc_597():
    lbl_new.config(text=list_c[596])
def fbtnc_598():
    lbl_new.config(text=list_c[597])
def fbtnc_599():
    lbl_new.config(text=list_c[598])
def fbtnc_600():
    lbl_new.config(text=list_c[599])
def fbtnc_601():
    lbl_new.config(text=list_c[600])
def fbtnc_602():
    lbl_new.config(text=list_c[601])
def fbtnc_603():
    lbl_new.config(text=list_c[602])
def fbtnc_604():
    lbl_new.config(text=list_c[603])
def fbtnc_605():
    lbl_new.config(text=list_c[604])
def fbtnc_606():
    lbl_new.config(text=list_c[605])
def fbtnc_607():
    lbl_new.config(text=list_c[606])
def fbtnc_608():
    lbl_new.config(text=list_c[607])
def fbtnc_609():
    lbl_new.config(text=list_c[608])
def fbtnc_610():
    lbl_new.config(text=list_c[609])
def fbtnc_611():
    lbl_new.config(text=list_c[610])
def fbtnc_612():
    lbl_new.config(text=list_c[611])
def fbtnc_613():
    lbl_new.config(text=list_c[612])
def fbtnc_614():
    lbl_new.config(text=list_c[613])
def fbtnc_615():
    lbl_new.config(text=list_c[614])
def fbtnc_616():
    lbl_new.config(text=list_c[615])
def fbtnc_617():
    lbl_new.config(text=list_c[616])
def fbtnc_618():
    lbl_new.config(text=list_c[617])
def fbtnc_619():
    lbl_new.config(text=list_c[618])
def fbtnc_620():
    lbl_new.config(text=list_c[619])
def fbtnc_621():
    lbl_new.config(text=list_c[620])
def fbtnc_622():
    lbl_new.config(text=list_c[621])
def fbtnc_623():
    lbl_new.config(text=list_c[622])
def fbtnc_624():
    lbl_new.config(text=list_c[623])
def fbtnc_625():
    lbl_new.config(text=list_c[624])
def fbtnc_626():
    lbl_new.config(text=list_c[625])
def fbtnc_627():
    lbl_new.config(text=list_c[626])
def fbtnc_628():
    lbl_new.config(text=list_c[627])
def fbtnc_629():
    lbl_new.config(text=list_c[628])
def fbtnc_630():
    lbl_new.config(text=list_c[629])
def fbtnc_631():
    lbl_new.config(text=list_c[630])
def fbtnc_632():
    lbl_new.config(text=list_c[631])
def fbtnc_633():
    lbl_new.config(text=list_c[632])
def fbtnc_634():
    lbl_new.config(text=list_c[633])
def fbtnc_635():
    lbl_new.config(text=list_c[634])
def fbtnc_636():
    lbl_new.config(text=list_c[635])
def fbtnc_637():
    lbl_new.config(text=list_c[636])
def fbtnc_638():
    lbl_new.config(text=list_c[637])
def fbtnc_639():
    lbl_new.config(text=list_c[638])
def fbtnc_640():
    lbl_new.config(text=list_c[639])
def fbtnc_641():
    lbl_new.config(text=list_c[640])
def fbtnc_642():
    lbl_new.config(text=list_c[641])
def fbtnc_643():
    lbl_new.config(text=list_c[642])
def fbtnc_644():
    lbl_new.config(text=list_c[643])
def fbtnc_645():
    lbl_new.config(text=list_c[644])
def fbtnc_646():
    lbl_new.config(text=list_c[645])
def fbtnc_647():
    lbl_new.config(text=list_c[646])
def fbtnc_648():
    lbl_new.config(text=list_c[647])
def fbtnc_649():
    lbl_new.config(text=list_c[648])
def fbtnc_650():
    lbl_new.config(text=list_c[649])
def fbtnc_651():
    lbl_new.config(text=list_c[650])
def fbtnc_652():
    lbl_new.config(text=list_c[651])
def fbtnc_653():
    lbl_new.config(text=list_c[652])
def fbtnc_654():
    lbl_new.config(text=list_c[653])
def fbtnc_655():
    lbl_new.config(text=list_c[654])
def fbtnc_656():
    lbl_new.config(text=list_c[655])
def fbtnc_657():
    lbl_new.config(text=list_c[656])
def fbtnc_658():
    lbl_new.config(text=list_c[657])
def fbtnc_659():
    lbl_new.config(text=list_c[658])
def fbtnc_660():
    lbl_new.config(text=list_c[659])
def fbtnc_661():
    lbl_new.config(text=list_c[660])
def fbtnc_662():
    lbl_new.config(text=list_c[661])
def fbtnc_663():
    lbl_new.config(text=list_c[662])
def fbtnc_664():
    lbl_new.config(text=list_c[663])
def fbtnc_665():
    lbl_new.config(text=list_c[664])
def fbtnc_666():
    lbl_new.config(text=list_c[665])
def fbtnc_667():
    lbl_new.config(text=list_c[666])
def fbtnc_668():
    lbl_new.config(text=list_c[667])
def fbtnc_669():
    lbl_new.config(text=list_c[668])
def fbtnc_670():
    lbl_new.config(text=list_c[669])
def fbtnc_671():
    lbl_new.config(text=list_c[670])
def fbtnc_672():
    lbl_new.config(text=list_c[671])
def fbtnc_673():
    lbl_new.config(text=list_c[672])
def fbtnc_674():
    lbl_new.config(text=list_c[673])
def fbtnc_675():
    lbl_new.config(text=list_c[674])
def fbtnc_676():
    lbl_new.config(text=list_c[675])
def fbtnc_677():
    lbl_new.config(text=list_c[676])
def fbtnc_678():
    lbl_new.config(text=list_c[677])
def fbtnc_679():
    lbl_new.config(text=list_c[678])
def fbtnc_680():
    lbl_new.config(text=list_c[679])
def fbtnc_681():
    lbl_new.config(text=list_c[680])
def fbtnc_682():
    lbl_new.config(text=list_c[681])
def fbtnc_683():
    lbl_new.config(text=list_c[682])
def fbtnc_684():
    lbl_new.config(text=list_c[683])
def fbtnc_685():
    lbl_new.config(text=list_c[684])
def fbtnc_686():
    lbl_new.config(text=list_c[685])
def fbtnc_687():
    lbl_new.config(text=list_c[686])
def fbtnc_688():
    lbl_new.config(text=list_c[687])
def fbtnc_689():
    lbl_new.config(text=list_c[688])
def fbtnc_690():
    lbl_new.config(text=list_c[689])
def fbtnc_691():
    lbl_new.config(text=list_c[690])
def fbtnc_692():
    lbl_new.config(text=list_c[691])
def fbtnc_693():
    lbl_new.config(text=list_c[692])
def fbtnc_694():
    lbl_new.config(text=list_c[693])
def fbtnc_695():
    lbl_new.config(text=list_c[694])
def fbtnc_696():
    lbl_new.config(text=list_c[695])
def fbtnc_697():
    lbl_new.config(text=list_c[696])
def fbtnc_698():
    lbl_new.config(text=list_c[697])
def fbtnc_699():
    lbl_new.config(text=list_c[698])
def fbtnc_700():
    lbl_new.config(text=list_c[699])
def fbtnc_701():
    lbl_new.config(text=list_c[700])
def fbtnc_702():
    lbl_new.config(text=list_c[701])
def fbtnc_703():
    lbl_new.config(text=list_c[702])
def fbtnc_704():
    lbl_new.config(text=list_c[703])
def fbtnc_705():
    lbl_new.config(text=list_c[704])
def fbtnc_706():
    lbl_new.config(text=list_c[705])
def fbtnc_707():
    lbl_new.config(text=list_c[706])
def fbtnc_708():
    lbl_new.config(text=list_c[707])
def fbtnc_709():
    lbl_new.config(text=list_c[708])
def fbtnc_710():
    lbl_new.config(text=list_c[709])
def fbtnc_711():
    lbl_new.config(text=list_c[710])
def fbtnc_712():
    lbl_new.config(text=list_c[711])
def fbtnc_713():
    lbl_new.config(text=list_c[712])
def fbtnc_714():
    lbl_new.config(text=list_c[713])
def fbtnc_715():
    lbl_new.config(text=list_c[714])
def fbtnc_716():
    lbl_new.config(text=list_c[715])
def fbtnc_717():
    lbl_new.config(text=list_c[716])
def fbtnc_718():
    lbl_new.config(text=list_c[717])
def fbtnc_719():
    lbl_new.config(text=list_c[718])
def fbtnc_720():
    lbl_new.config(text=list_c[719])
def fbtnc_721():
    lbl_new.config(text=list_c[720])
def fbtnc_722():
    lbl_new.config(text=list_c[721])
def fbtnc_723():
    lbl_new.config(text=list_c[722])
def fbtnc_724():
    lbl_new.config(text=list_c[723])
def fbtnc_725():
    lbl_new.config(text=list_c[724])
def fbtnc_726():
    lbl_new.config(text=list_c[725])
def fbtnc_727():
    lbl_new.config(text=list_c[726])
def fbtnc_728():
    lbl_new.config(text=list_c[727])
def fbtnc_729():
    lbl_new.config(text=list_c[728])
def fbtnc_730():
    lbl_new.config(text=list_c[729])
def fbtnc_731():
    lbl_new.config(text=list_c[730])
def fbtnc_732():
    lbl_new.config(text=list_c[731])
def fbtnc_733():
    lbl_new.config(text=list_c[732])
def fbtnc_734():
    lbl_new.config(text=list_c[733])
def fbtnc_735():
    lbl_new.config(text=list_c[734])
def fbtnc_736():
    lbl_new.config(text=list_c[735])
def fbtnc_737():
    lbl_new.config(text=list_c[736])
def fbtnc_738():
    lbl_new.config(text=list_c[737])
def fbtnc_739():
    lbl_new.config(text=list_c[738])
def fbtnc_740():
    lbl_new.config(text=list_c[739])
def fbtnc_741():
    lbl_new.config(text=list_c[740])
def fbtnc_742():
    lbl_new.config(text=list_c[741])
def fbtnc_743():
    lbl_new.config(text=list_c[742])
def fbtnc_744():
    lbl_new.config(text=list_c[743])
def fbtnc_745():
    lbl_new.config(text=list_c[744])
def fbtnc_746():
    lbl_new.config(text=list_c[745])
def fbtnc_747():
    lbl_new.config(text=list_c[746])
def fbtnc_748():
    lbl_new.config(text=list_c[747])
def fbtnc_749():
    lbl_new.config(text=list_c[748])
def fbtnc_750():
    lbl_new.config(text=list_c[749])
def fbtnc_751():
    lbl_new.config(text=list_c[750])
def fbtnc_752():
    lbl_new.config(text=list_c[751])
def fbtnc_753():
    lbl_new.config(text=list_c[752])
def fbtnc_754():
    lbl_new.config(text=list_c[753])
def fbtnc_755():
    lbl_new.config(text=list_c[754])
def fbtnc_756():
    lbl_new.config(text=list_c[755])
def fbtnc_757():
    lbl_new.config(text=list_c[756])
def fbtnc_758():
    lbl_new.config(text=list_c[757])
def fbtnc_759():
    lbl_new.config(text=list_c[758])
def fbtnc_760():
    lbl_new.config(text=list_c[759])
def fbtnc_761():
    lbl_new.config(text=list_c[760])
def fbtnc_762():
    lbl_new.config(text=list_c[761])
def fbtnc_763():
    lbl_new.config(text=list_c[762])
def fbtnc_764():
    lbl_new.config(text=list_c[763])
def fbtnc_765():
    lbl_new.config(text=list_c[764])
def fbtnc_766():
    lbl_new.config(text=list_c[765])
def fbtnc_767():
    lbl_new.config(text=list_c[766])
def fbtnc_768():
    lbl_new.config(text=list_c[767])
def fbtnc_769():
    lbl_new.config(text=list_c[768])
def fbtnc_770():
    lbl_new.config(text=list_c[769])
def fbtnc_771():
    lbl_new.config(text=list_c[770])
def fbtnc_772():
    lbl_new.config(text=list_c[771])
def fbtnc_773():
    lbl_new.config(text=list_c[772])
def fbtnc_774():
    lbl_new.config(text=list_c[773])
def fbtnc_775():
    lbl_new.config(text=list_c[774])
def fbtnc_776():
    lbl_new.config(text=list_c[775])
def fbtnc_777():
    lbl_new.config(text=list_c[776])
def fbtnc_778():
    lbl_new.config(text=list_c[777])
def fbtnc_779():
    lbl_new.config(text=list_c[778])
def fbtnc_780():
    lbl_new.config(text=list_c[779])
def fbtnc_781():
    lbl_new.config(text=list_c[780])
def fbtnc_782():
    lbl_new.config(text=list_c[781])
def fbtnc_783():
    lbl_new.config(text=list_c[782])
def fbtnc_784():
    lbl_new.config(text=list_c[783])
def fbtnc_785():
    lbl_new.config(text=list_c[784])
def fbtnc_786():
    lbl_new.config(text=list_c[785])
def fbtnc_787():
    lbl_new.config(text=list_c[786])
def fbtnc_788():
    lbl_new.config(text=list_c[787])
def fbtnc_789():
    lbl_new.config(text=list_c[788])
def fbtnc_790():
    lbl_new.config(text=list_c[789])
def fbtnc_791():
    lbl_new.config(text=list_c[790])
def fbtnc_792():
    lbl_new.config(text=list_c[791])
def fbtnc_793():
    lbl_new.config(text=list_c[792])
def fbtnc_794():
    lbl_new.config(text=list_c[793])
def fbtnc_795():
    lbl_new.config(text=list_c[794])
def fbtnc_796():
    lbl_new.config(text=list_c[795])
def fbtnc_797():
    lbl_new.config(text=list_c[796])
def fbtnc_798():
    lbl_new.config(text=list_c[797])
def fbtnc_799():
    lbl_new.config(text=list_c[798])
def fbtnc_800():
    lbl_new.config(text=list_c[799])
def fbtnc_801():
    lbl_new.config(text=list_c[800])
def fbtnc_802():
    lbl_new.config(text=list_c[801])
def fbtnc_803():
    lbl_new.config(text=list_c[802])
def fbtnc_804():
    lbl_new.config(text=list_c[803])
def fbtnc_805():
    lbl_new.config(text=list_c[804])
def fbtnc_806():
    lbl_new.config(text=list_c[805])
def fbtnc_807():
    lbl_new.config(text=list_c[806])
def fbtnc_808():
    lbl_new.config(text=list_c[807])
def fbtnc_809():
    lbl_new.config(text=list_c[808])
def fbtnc_810():
    lbl_new.config(text=list_c[809])
def fbtnc_811():
    lbl_new.config(text=list_c[810])
def fbtnc_812():
    lbl_new.config(text=list_c[811])
def fbtnc_813():
    lbl_new.config(text=list_c[812])
def fbtnc_814():
    lbl_new.config(text=list_c[813])
def fbtnc_815():
    lbl_new.config(text=list_c[814])
def fbtnc_816():
    lbl_new.config(text=list_c[815])
def fbtnc_817():
    lbl_new.config(text=list_c[816])
def fbtnc_818():
    lbl_new.config(text=list_c[817])
def fbtnc_819():
    lbl_new.config(text=list_c[818])
def fbtnc_820():
    lbl_new.config(text=list_c[819])
def fbtnc_821():
    lbl_new.config(text=list_c[820])
def fbtnc_822():
    lbl_new.config(text=list_c[821])
def fbtnc_823():
    lbl_new.config(text=list_c[822])
def fbtnc_824():
    lbl_new.config(text=list_c[823])
def fbtnc_825():
    lbl_new.config(text=list_c[824])
def fbtnc_826():
    lbl_new.config(text=list_c[825])
def fbtnc_827():
    lbl_new.config(text=list_c[826])
def fbtnc_828():
    lbl_new.config(text=list_c[827])
def fbtnc_829():
    lbl_new.config(text=list_c[828])
def fbtnc_830():
    lbl_new.config(text=list_c[829])
def fbtnc_831():
    lbl_new.config(text=list_c[830])
def fbtnc_832():
    lbl_new.config(text=list_c[831])
def fbtnc_833():
    lbl_new.config(text=list_c[832])
def fbtnc_834():
    lbl_new.config(text=list_c[833])
def fbtnc_835():
    lbl_new.config(text=list_c[834])
def fbtnc_836():
    lbl_new.config(text=list_c[835])
def fbtnc_837():
    lbl_new.config(text=list_c[836])
def fbtnc_838():
    lbl_new.config(text=list_c[837])
def fbtnc_839():
    lbl_new.config(text=list_c[838])
def fbtnc_840():
    lbl_new.config(text=list_c[839])
def fbtnc_841():
    lbl_new.config(text=list_c[840])
def fbtnc_842():
    lbl_new.config(text=list_c[841])
def fbtnc_843():
    lbl_new.config(text=list_c[842])
def fbtnc_844():
    lbl_new.config(text=list_c[843])
def fbtnc_845():
    lbl_new.config(text=list_c[844])
def fbtnc_846():
    lbl_new.config(text=list_c[845])
def fbtnc_847():
    lbl_new.config(text=list_c[846])
def fbtnc_848():
    lbl_new.config(text=list_c[847])
def fbtnc_849():
    lbl_new.config(text=list_c[848])
def fbtnc_850():
    lbl_new.config(text=list_c[849])
def fbtnc_851():
    lbl_new.config(text=list_c[850])
def fbtnc_852():
    lbl_new.config(text=list_c[851])
def fbtnc_853():
    lbl_new.config(text=list_c[852])
def fbtnc_854():
    lbl_new.config(text=list_c[853])
def fbtnc_855():
    lbl_new.config(text=list_c[854])
def fbtnc_856():
    lbl_new.config(text=list_c[855])
def fbtnc_857():
    lbl_new.config(text=list_c[856])
def fbtnc_858():
    lbl_new.config(text=list_c[857])
def fbtnc_859():
    lbl_new.config(text=list_c[858])
def fbtnc_860():
    lbl_new.config(text=list_c[859])
def fbtnc_861():
    lbl_new.config(text=list_c[860])
def fbtnc_862():
    lbl_new.config(text=list_c[861])
def fbtnc_863():
    lbl_new.config(text=list_c[862])
def fbtnc_864():
    lbl_new.config(text=list_c[863])
def fbtnc_865():
    lbl_new.config(text=list_c[864])
def fbtnc_866():
    lbl_new.config(text=list_c[865])
def fbtnc_867():
    lbl_new.config(text=list_c[866])
def fbtnc_868():
    lbl_new.config(text=list_c[867])
def fbtnc_869():
    lbl_new.config(text=list_c[868])
def fbtnc_870():
    lbl_new.config(text=list_c[869])
def fbtnc_871():
    lbl_new.config(text=list_c[870])
def fbtnc_872():
    lbl_new.config(text=list_c[871])
def fbtnc_873():
    lbl_new.config(text=list_c[872])
def fbtnc_874():
    lbl_new.config(text=list_c[873])
def fbtnc_875():
    lbl_new.config(text=list_c[874])
def fbtnc_876():
    lbl_new.config(text=list_c[875])
def fbtnc_877():
    lbl_new.config(text=list_c[876])
def fbtnc_878():
    lbl_new.config(text=list_c[877])
def fbtnc_879():
    lbl_new.config(text=list_c[878])
def fbtnc_880():
    lbl_new.config(text=list_c[879])
def fbtnc_881():
    lbl_new.config(text=list_c[880])
def fbtnc_882():
    lbl_new.config(text=list_c[881])
def fbtnc_883():
    lbl_new.config(text=list_c[882])
def fbtnc_884():
    lbl_new.config(text=list_c[883])
def fbtnc_885():
    lbl_new.config(text=list_c[884])
def fbtnc_886():
    lbl_new.config(text=list_c[885])
def fbtnc_887():
    lbl_new.config(text=list_c[886])
def fbtnc_888():
    lbl_new.config(text=list_c[887])
def fbtnc_889():
    lbl_new.config(text=list_c[888])
def fbtnc_890():
    lbl_new.config(text=list_c[889])
def fbtnc_891():
    lbl_new.config(text=list_c[890])
def fbtnc_892():
    lbl_new.config(text=list_c[891])
def fbtnc_893():
    lbl_new.config(text=list_c[892])
def fbtnc_894():
    lbl_new.config(text=list_c[893])
def fbtnc_895():
    lbl_new.config(text=list_c[894])
def fbtnc_896():
    lbl_new.config(text=list_c[895])
def fbtnc_897():
    lbl_new.config(text=list_c[896])
def fbtnc_898():
    lbl_new.config(text=list_c[897])
def fbtnc_899():
    lbl_new.config(text=list_c[898])
def fbtnc_900():
    lbl_new.config(text=list_c[899])
def fbtnc_901():
    lbl_new.config(text=list_c[900])
def fbtnc_902():
    lbl_new.config(text=list_c[901])
def fbtnc_903():
    lbl_new.config(text=list_c[902])
def fbtnc_904():
    lbl_new.config(text=list_c[903])
def fbtnc_905():
    lbl_new.config(text=list_c[904])
def fbtnc_906():
    lbl_new.config(text=list_c[905])
def fbtnc_907():
    lbl_new.config(text=list_c[906])
def fbtnc_908():
    lbl_new.config(text=list_c[907])
def fbtnc_909():
    lbl_new.config(text=list_c[908])
def fbtnc_910():
    lbl_new.config(text=list_c[909])
def fbtnc_911():
    lbl_new.config(text=list_c[910])
def fbtnc_912():
    lbl_new.config(text=list_c[911])
def fbtnc_913():
    lbl_new.config(text=list_c[912])
def fbtnc_914():
    lbl_new.config(text=list_c[913])
def fbtnc_915():
    lbl_new.config(text=list_c[914])
def fbtnc_916():
    lbl_new.config(text=list_c[915])
def fbtnc_917():
    lbl_new.config(text=list_c[916])
def fbtnc_918():
    lbl_new.config(text=list_c[917])
def fbtnc_919():
    lbl_new.config(text=list_c[918])
def fbtnc_920():
    lbl_new.config(text=list_c[919])
def fbtnc_921():
    lbl_new.config(text=list_c[920])
def fbtnc_922():
    lbl_new.config(text=list_c[921])
def fbtnc_923():
    lbl_new.config(text=list_c[922])
def fbtnc_924():
    lbl_new.config(text=list_c[923])
def fbtnc_925():
    lbl_new.config(text=list_c[924])
def fbtnc_926():
    lbl_new.config(text=list_c[925])
def fbtnc_927():
    lbl_new.config(text=list_c[926])
def fbtnc_928():
    lbl_new.config(text=list_c[927])
def fbtnc_929():
    lbl_new.config(text=list_c[928])
def fbtnc_930():
    lbl_new.config(text=list_c[929])
def fbtnc_931():
    lbl_new.config(text=list_c[930])
def fbtnc_932():
    lbl_new.config(text=list_c[931])
def fbtnc_933():
    lbl_new.config(text=list_c[932])
def fbtnc_934():
    lbl_new.config(text=list_c[933])
def fbtnc_935():
    lbl_new.config(text=list_c[934])
def fbtnc_936():
    lbl_new.config(text=list_c[935])
def fbtnc_937():
    lbl_new.config(text=list_c[936])
def fbtnc_938():
    lbl_new.config(text=list_c[937])
def fbtnc_939():
    lbl_new.config(text=list_c[938])
def fbtnc_940():
    lbl_new.config(text=list_c[939])
def fbtnc_941():
    lbl_new.config(text=list_c[940])
def fbtnc_942():
    lbl_new.config(text=list_c[941])
def fbtnc_943():
    lbl_new.config(text=list_c[942])
def fbtnc_944():
    lbl_new.config(text=list_c[943])
def fbtnc_945():
    lbl_new.config(text=list_c[944])
def fbtnc_946():
    lbl_new.config(text=list_c[945])
def fbtnc_947():
    lbl_new.config(text=list_c[946])
def fbtnc_948():
    lbl_new.config(text=list_c[947])
def fbtnc_949():
    lbl_new.config(text=list_c[948])
def fbtnc_950():
    lbl_new.config(text=list_c[949])
def fbtnc_951():
    lbl_new.config(text=list_c[950])
def fbtnc_952():
    lbl_new.config(text=list_c[951])
def fbtnc_953():
    lbl_new.config(text=list_c[952])
def fbtnc_954():
    lbl_new.config(text=list_c[953])
def fbtnc_955():
    lbl_new.config(text=list_c[954])
def fbtnc_956():
    lbl_new.config(text=list_c[955])
def fbtnc_957():
    lbl_new.config(text=list_c[956])
def fbtnc_958():
    lbl_new.config(text=list_c[957])
def fbtnc_959():
    lbl_new.config(text=list_c[958])
def fbtnc_960():
    lbl_new.config(text=list_c[959])
def fbtnc_961():
    lbl_new.config(text=list_c[960])
def fbtnc_962():
    lbl_new.config(text=list_c[961])
def fbtnc_963():
    lbl_new.config(text=list_c[962])
def fbtnc_964():
    lbl_new.config(text=list_c[963])
def fbtnc_965():
    lbl_new.config(text=list_c[964])
def fbtnc_966():
    lbl_new.config(text=list_c[965])
def fbtnc_967():
    lbl_new.config(text=list_c[966])
def fbtnc_968():
    lbl_new.config(text=list_c[967])
def fbtnc_969():
    lbl_new.config(text=list_c[968])
def fbtnc_970():
    lbl_new.config(text=list_c[969])
def fbtnc_971():
    lbl_new.config(text=list_c[970])
def fbtnc_972():
    lbl_new.config(text=list_c[971])
def fbtnc_973():
    lbl_new.config(text=list_c[972])
def fbtnc_974():
    lbl_new.config(text=list_c[973])
def fbtnc_975():
    lbl_new.config(text=list_c[974])
def fbtnc_976():
    lbl_new.config(text=list_c[975])
def fbtnc_977():
    lbl_new.config(text=list_c[976])
def fbtnc_978():
    lbl_new.config(text=list_c[977])
def fbtnc_979():
    lbl_new.config(text=list_c[978])
def fbtnc_980():
    lbl_new.config(text=list_c[979])
def fbtnc_981():
    lbl_new.config(text=list_c[980])
def fbtnc_982():
    lbl_new.config(text=list_c[981])
def fbtnc_983():
    lbl_new.config(text=list_c[982])
def fbtnc_984():
    lbl_new.config(text=list_c[983])
def fbtnc_985():
    lbl_new.config(text=list_c[984])
def fbtnc_986():
    lbl_new.config(text=list_c[985])
def fbtnc_987():
    lbl_new.config(text=list_c[986])
def fbtnc_988():
    lbl_new.config(text=list_c[987])
def fbtnc_989():
    lbl_new.config(text=list_c[988])
def fbtnc_990():
    lbl_new.config(text=list_c[989])
def fbtnc_991():
    lbl_new.config(text=list_c[990])
def fbtnc_992():
    lbl_new.config(text=list_c[991])
def fbtnc_993():
    lbl_new.config(text=list_c[992])
def fbtnc_994():
    lbl_new.config(text=list_c[993])
def fbtnc_995():
    lbl_new.config(text=list_c[994])
def fbtnc_996():
    lbl_new.config(text=list_c[995])
def fbtnc_997():
    lbl_new.config(text=list_c[996])
def fbtnc_998():
    lbl_new.config(text=list_c[997])
def fbtnc_999():
    lbl_new.config(text=list_c[998])
def fbtnc_1000():
    lbl_new.config(text=list_c[999])
def fbtnc_1001():
    lbl_new.config(text=list_c[1000])
def fbtnc_1002():
    lbl_new.config(text=list_c[1001])
def fbtnc_1003():
    lbl_new.config(text=list_c[1002])
def fbtnc_1004():
    lbl_new.config(text=list_c[1003])
def fbtnc_1005():
    lbl_new.config(text=list_c[1004])
def fbtnc_1006():
    lbl_new.config(text=list_c[1005])
def fbtnc_1007():
    lbl_new.config(text=list_c[1006])
def fbtnc_1008():
    lbl_new.config(text=list_c[1007])
def fbtnc_1009():
    lbl_new.config(text=list_c[1008])
def fbtnc_1010():
    lbl_new.config(text=list_c[1009])
def fbtnc_1011():
    lbl_new.config(text=list_c[1010])
def fbtnc_1012():
    lbl_new.config(text=list_c[1011])
def fbtnc_1013():
    lbl_new.config(text=list_c[1012])
def fbtnc_1014():
    lbl_new.config(text=list_c[1013])
def fbtnc_1015():
    lbl_new.config(text=list_c[1014])
def fbtnc_1016():
    lbl_new.config(text=list_c[1015])
def fbtnc_1017():
    lbl_new.config(text=list_c[1016])
def fbtnc_1018():
    lbl_new.config(text=list_c[1017])

def xplore() :
    root.config(bg="#f15bb5")
    frm_home.config(bg="#f15bb5")
    lbl_home.config(bg="#f15bb5")
    frm_L.pack_forget()
    frm_L2.pack_forget()
    main_frm.pack_forget()
    frm_new.pack(pady=20)
    lbl_new.pack()
    big_frm.pack()
    frm_nb.pack()

def make_a_palette() :
    root.config(bg="#ccff33")
    frm_home.config(bg="#ccff33")
    lbl_home.config(bg="#ccff33")
    frm_L.pack_forget()
    frm_L2.pack_forget()
    main_frm.pack_forget()
    frm_L3.pack(pady=10)
    frm_mkp.pack()

def home() :
    root.config(bg="#2ec4b6")
    frm_home.config(bg="#2ec4b6")
    lbl_home.config(bg="#2ec4b6")
    global summ
    main_frm.pack()
    frm_L2.pack(pady=100)
    frm_L.pack()
    frm_new.pack_forget()
    lbl_new.pack_forget()
    list_bigfrm[summ].pack_forget()
    frm_nb.pack_forget()
    frm_mkp.pack_forget()
    frm_L3.pack_forget()
    summ=0

summ = 0

def next() :
    global summ
    global list_bigfrm
    if summ == 7 :
        summ=6
    list_bigfrm[summ].pack_forget()
    frm_nb.pack_forget()
    summ=summ+1
    list_bigfrm[summ].pack()
    frm_nb.pack()


def back() :
    global summ
    global list_bigfrm
    if summ > 0 :
        list_bigfrm[summ].pack_forget()
        frm_nb.pack_forget()
        summ=summ-1
        list_bigfrm[summ].pack()
        frm_nb.pack()
    else :
        pass


def Random() :
    list_mkp=list_c2
    a=random.choice(list_mkp)
    list_mkp.remove(a)
    b=random.choice(list_mkp)
    list_mkp.remove(b)
    c=random.choice(list_mkp)
    list_mkp.remove(c)
    d=random.choice(list_mkp)
    list_mkp.remove(d)
    e=random.choice(list_mkp)
    list_mkp.remove(e)
    btnc_mkp_1.config(bg=a)
    btnc_mkp_2.config(bg=b)
    btnc_mkp_3.config(bg=c)
    btnc_mkp_4.config(bg=d)
    btnc_mkp_5.config(bg=e)

def fbtnc_mkp1() :
    lbl_mkp.config(text=btnc_mkp_1['bg'])
def fbtnc_mkp2() :
    lbl_mkp.config(text=btnc_mkp_2['bg'])
def fbtnc_mkp3() :
    lbl_mkp.config(text=btnc_mkp_3['bg'])
def fbtnc_mkp4() :
    lbl_mkp.config(text=btnc_mkp_4['bg'])
def fbtnc_mkp5() :
    lbl_mkp.config(text=btnc_mkp_5['bg'])






# root

root = Tk()

root.title("Colors")
root.geometry("1300x900+250+50")
root.resizable(1,1)
root.config(bg="#2ec4b6")








#Home

frm_home = Frame(root, bg="#2ec4b6")
frm_home.pack()

btn_home = Button(frm_home, text="HOME", bg="#70e000", font=('Comic Sans MS',14), fg="black", command=home)
btn_home.grid(row=0, column=1, pady=5)
lbl_home= Label(frm_home, bg="#2ec4b6")
lbl_home.grid(row=0, column=0, padx=605, pady=5)

main_frm = Frame(root, bg="#2ec4b6")
main_frm.pack()

frm_L2 = Frame(root, width=1120, height=100)
frm_L2.pack(pady=100)

lbl__1 = Label(frm_L2,text="W", bg="#b8c0ff", font=("Comic Sans MS",40), fg="black")
lbl__1.grid(row=0,column=0)
lbl__2 = Label(frm_L2,text="E", bg="#ffeedd", font=("Comic Sans MS",40), fg="black")
lbl__2.grid(row=0,column=1)
lbl__3 = Label(frm_L2,text="L", bg="#43aa8b", font=("Comic Sans MS",40), fg="black")
lbl__3.grid(row=0,column=2)
lbl__4 = Label(frm_L2,text="C", bg="#941b0c", font=("Comic Sans MS",40), fg="black")
lbl__4.grid(row=0,column=3)
lbl__5 = Label(frm_L2,text="O", bg="#e9ff70", font=("Comic Sans MS",40), fg="black")
lbl__5.grid(row=0,column=4)
lbl__6 = Label(frm_L2,text="M", bg="#d00000", font=("Comic Sans MS",40), fg="black")
lbl__6.grid(row=0,column=5)
lbl__7 = Label(frm_L2,text="E", bg="#736ced", font=("Comic Sans MS",40), fg="black")
lbl__7.grid(row=0,column=6)



frm_L = Frame(root, width=1120, height=100, bg="lightblue")
frm_L.pack()

lbl_1 = Label(frm_L,text="C", bg="#3C91E6", font=("Comic Sans MS",40), fg="black")
lbl_1.grid(row=0,column=0)
lbl_2 = Label(frm_L,text="H", bg="#342E37", font=("Comic Sans MS",40), fg="black")
lbl_2.grid(row=0,column=1)
lbl_3 = Label(frm_L,text="O", bg="#A2D729", font=("Comic Sans MS",40), fg="black")
lbl_3.grid(row=0,column=2)
lbl_4 = Label(frm_L,text="O", bg="#FAFFFD", font=("Comic Sans MS",40), fg="black")
lbl_4.grid(row=0,column=3)
lbl_5 = Label(frm_L,text="S", bg="#800f2f", font=("Comic Sans MS",40), fg="black")
lbl_5.grid(row=0,column=4)
lbl_6 = Label(frm_L,text="E", bg="#fb8500", font=("Comic Sans MS",40), fg="black")
lbl_6.grid(row=0,column=5)
lbl_7 = Label(frm_L,text="_", bg="#8338ec", font=("Comic Sans MS",40), fg="black")
lbl_7.grid(row=0,column=6)
lbl_8 = Label(frm_L,text="A", bg="#3a86ff", font=("Comic Sans MS",40), fg="black")
lbl_8.grid(row=0,column=7)
lbl_9 = Label(frm_L,text="_", bg="#ffb700", font=("Comic Sans MS",40), fg="black")
lbl_9.grid(row=0,column=8)
lbl_10 = Label(frm_L,text="C", bg="#d62828", font=("Comic Sans MS",40), fg="black")
lbl_10.grid(row=0,column=9)
lbl_11 = Label(frm_L,text="O", bg="#f2e8cf", font=("Comic Sans MS",40), fg="black")
lbl_11.grid(row=0,column=10)
lbl_12 = Label(frm_L,text="L", bg="#ff8fab", font=("Comic Sans MS",40), fg="black")
lbl_12.grid(row=0,column=11)
lbl_13 = Label(frm_L,text="O", bg="#4d908e", font=("Comic Sans MS",40), fg="black")
lbl_13.grid(row=0,column=12)
lbl_14 = Label(frm_L,text="R", bg="#ffd6ff", font=("Comic Sans MS",40), fg="black")
lbl_14.grid(row=0,column=13)



frm_1 = Frame(main_frm)
frm_1.grid(row=0, column=0, padx=235.5, pady=120)

frm_2 = Frame(main_frm)
frm_2.grid(row=0, column=1, padx=235.5, pady=120)

btn_1 = Button(frm_1,width=15, text="XPLORE", font=("Comic Sans MS",14), bg="#219ebc", command=xplore)
btn_1.pack()

btn_2 = Button(frm_2, width=15, text="MAKE A PALETTE", font=("Comic Sans MS",14), bg="#ff006e", command=make_a_palette)
btn_2.pack()










#Xplore

frm_new = Frame(root)

lbl__1 = Label(frm_new,text="X", bg="#b8c0ff", font=("Comic Sans MS",40), fg="black")
lbl__1.grid(row=0,column=0)
lbl__2 = Label(frm_new,text="P", bg="#ffeedd", font=("Comic Sans MS",40), fg="black")
lbl__2.grid(row=0,column=1)
lbl__3 = Label(frm_new,text="L", bg="#43aa8b", font=("Comic Sans MS",40), fg="black")
lbl__3.grid(row=0,column=2)
lbl__4 = Label(frm_new,text="O", bg="#941b0c", font=("Comic Sans MS",40), fg="black")
lbl__4.grid(row=0,column=3)
lbl__5 = Label(frm_new,text="R", bg="#e9ff70", font=("Comic Sans MS",40), fg="black")
lbl__5.grid(row=0,column=4)
lbl__6 = Label(frm_new,text="E", bg="#d00000", font=("Comic Sans MS",40), fg="black")
lbl__6.grid(row=0,column=5)

lbl_new = Label(root,width=12, text="", bg="white", font=("Comic Sans Ms", 24), fg='black')

frm_nb = Frame(root, bg="#f15bb5")

btn_next = Button(frm_nb, text="NEXT", font=("Comic Sans MS",14), fg="black", bg="#70e000", command=next)
btn_next.grid(row=0, column=1, padx=65, pady=5)

btn_back = Button(frm_nb, text="BACK", font=("Comic Sans MS",14), fg="black", bg="#70e000", command=back)
btn_back.grid(row=0, column=0, padx=65, pady=5)





#MKP

frm_L3 = Frame(root)

lbl_1 = Label(frm_L3,text="M", bg="#3C91E6", font=("Comic Sans MS",40), fg="black")
lbl_1.grid(row=0,column=0)
lbl_2 = Label(frm_L3,text="A", bg="#342E37", font=("Comic Sans MS",40), fg="black")
lbl_2.grid(row=0,column=1)
lbl_3 = Label(frm_L3,text="K", bg="#A2D729", font=("Comic Sans MS",40), fg="black")
lbl_3.grid(row=0,column=2)
lbl_4 = Label(frm_L3,text="E", bg="#FAFFFD", font=("Comic Sans MS",40), fg="black")
lbl_4.grid(row=0,column=3)
lbl_5 = Label(frm_L3,text="_", bg="#800f2f", font=("Comic Sans MS",40), fg="black")
lbl_5.grid(row=0,column=4)
lbl_6 = Label(frm_L3,text="A", bg="#fb8500", font=("Comic Sans MS",40), fg="black")
lbl_6.grid(row=0,column=5)
lbl_7 = Label(frm_L3,text="_", bg="#8338ec", font=("Comic Sans MS",40), fg="black")
lbl_7.grid(row=0,column=6)
lbl_8 = Label(frm_L3,text="P", bg="#3a86ff", font=("Comic Sans MS",40), fg="black")
lbl_8.grid(row=0,column=7)
lbl_9 = Label(frm_L3,text="L", bg="#ffb700", font=("Comic Sans MS",40), fg="black")
lbl_9.grid(row=0,column=8)
lbl_10 = Label(frm_L3,text="A", bg="#d62828", font=("Comic Sans MS",40), fg="black")
lbl_10.grid(row=0,column=9)
lbl_11 = Label(frm_L3,text="T", bg="#f2e8cf", font=("Comic Sans MS",40), fg="black")
lbl_11.grid(row=0,column=10)
lbl_12 = Label(frm_L3,text="E", bg="#ff8fab", font=("Comic Sans MS",40), fg="black")
lbl_12.grid(row=0,column=11)

frm_mkp = Frame(root, bg="#ccff33")

lbl_mkp = Label(frm_mkp,width=12, text="", bg="white", font=("Comic Sans Ms", 24), fg='black')
lbl_mkp.grid(row=0, columnspan=5)

btnc_mkp_1 = Button(frm_mkp, font=("", 196), bg=random.choice(list_c),command=fbtnc_mkp1)
btnc_mkp_1.grid(row=1, column=0)
btnc_mkp_2 = Button(frm_mkp, font=("", 196), bg=random.choice(list_c),command=fbtnc_mkp2)
btnc_mkp_2.grid(row=1, column=1)
btnc_mkp_3 = Button(frm_mkp, font=("", 196), bg=random.choice(list_c),command=fbtnc_mkp3)
btnc_mkp_3.grid(row=1, column=2, pady=60)
btnc_mkp_4 = Button(frm_mkp, font=("", 196), bg=random.choice(list_c),command=fbtnc_mkp4)
btnc_mkp_4.grid(row=1, column=3)
btnc_mkp_5 = Button(frm_mkp, font=("", 196), bg=random.choice(list_c),command=fbtnc_mkp5)
btnc_mkp_5.grid(row=1, column=4)

btn_random = Button(frm_mkp, text="RANDOM", bg="#70e000", fg="black", font=("Comic Sans MS",14), command=Random)
btn_random.grid(row=2, columnspan=5)













#COLORS

big_frm = Frame(root, bg="#f15bb5")

frmc_1 = Frame(big_frm)
frmc_1.grid(row=0, column=0, padx=20)

btnc_1 = Button(frmc_1, bg=list_c[0], font=("", 36), command=fbtnc_1)
btnc_1.grid(row=0,column=0)
btnc_2 = Button(frmc_1, bg=list_c[1], font=("", 36), command=fbtnc_2)
btnc_2.grid(row=0,column=1)
btnc_3 = Button(frmc_1, bg=list_c[2], font=("", 36), command=fbtnc_3)
btnc_3.grid(row=0,column=2)
btnc_4 = Button(frmc_1, bg=list_c[3], font=("", 36), command=fbtnc_4)
btnc_4.grid(row=0,column=3)
btnc_5 = Button(frmc_1, bg=list_c[4], font=("", 36), command=fbtnc_5)
btnc_5.grid(row=0,column=4)


frmc_2 = Frame(big_frm)
frmc_2.grid(row=0, column=1)

btnc_6 = Button(frmc_2, bg=list_c[5], font=("", 36), command=fbtnc_6)
btnc_6.grid(row=0,column=0)
btnc_7 = Button(frmc_2, bg=list_c[6], font=("", 36), command=fbtnc_7)
btnc_7.grid(row=0,column=1)
btnc_8 = Button(frmc_2, bg=list_c[7], font=("", 36), command=fbtnc_8)
btnc_8.grid(row=0,column=2)
btnc_9 = Button(frmc_2, bg=list_c[8], font=("", 36), command=fbtnc_9)
btnc_9.grid(row=0,column=3)
btnc_10 = Button(frmc_2, bg=list_c[9], font=("", 36), command=fbtnc_10)
btnc_10.grid(row=0,column=4)



frmc_3 = Frame(big_frm)
frmc_3.grid(row=0, column=2, padx=20)

btnc_11 = Button(frmc_3, bg=list_c[10], font=("", 36), command=fbtnc_11)
btnc_11.grid(row=0,column=0)
btnc_12 = Button(frmc_3, bg=list_c[11], font=("", 36), command=fbtnc_12)
btnc_12.grid(row=0,column=1)
btnc_13 = Button(frmc_3, bg=list_c[12], font=("", 36), command=fbtnc_13)
btnc_13.grid(row=0,column=2)
btnc_14 = Button(frmc_3, bg=list_c[13], font=("", 36), command=fbtnc_14)
btnc_14.grid(row=0,column=3)
btnc_15 = Button(frmc_3, bg=list_c[14], font=("", 36), command=fbtnc_15)
btnc_15.grid(row=0,column=4)



frmc_4 = Frame(big_frm)
frmc_4.grid(row=0, column=3)

btnc_16 = Button(frmc_4, bg=list_c[15], font=("", 36), command=fbtnc_16)
btnc_16.grid(row=0,column=0)
btnc_17 = Button(frmc_4, bg=list_c[16], font=("", 36), command=fbtnc_17)
btnc_17.grid(row=0,column=1)
btnc_18 = Button(frmc_4, bg=list_c[17], font=("", 36), command=fbtnc_18)
btnc_18.grid(row=0,column=2)
btnc_19 = Button(frmc_4, bg=list_c[18], font=("", 36), command=fbtnc_19)
btnc_19.grid(row=0,column=3)
btnc_20 = Button(frmc_4, bg=list_c[19], font=("", 36), command=fbtnc_20)
btnc_20.grid(row=0,column=4)



frmc_5 = Frame(big_frm)
frmc_5.grid(row=0, column=4, padx=20, pady=20)

btnc_21 = Button(frmc_5, bg=list_c[20], font=("", 36), command=fbtnc_21)
btnc_21.grid(row=0,column=0)
btnc_22 = Button(frmc_5, bg=list_c[21], font=("", 36), command=fbtnc_22)
btnc_22.grid(row=0,column=1)
btnc_23 = Button(frmc_5, bg=list_c[22], font=("", 36), command=fbtnc_23)
btnc_23.grid(row=0,column=2)
btnc_24 = Button(frmc_5, bg=list_c[23], font=("", 36), command=fbtnc_24)
btnc_24.grid(row=0,column=3)
btnc_25 = Button(frmc_5, bg=list_c[24], font=("", 36), command=fbtnc_25)
btnc_25.grid(row=0,column=4)



frmc_6 = Frame(big_frm)
frmc_6.grid(row=1, column=0, padx=20)

btnc_26 = Button(frmc_6, bg=list_c[25], font=("", 36), command=fbtnc_26)
btnc_26.grid(row=0,column=0)
btnc_27 = Button(frmc_6, bg=list_c[26], font=("", 36), command=fbtnc_27)
btnc_27.grid(row=0,column=1)
btnc_28 = Button(frmc_6, bg=list_c[27], font=("", 36), command=fbtnc_28)
btnc_28.grid(row=0,column=2)
btnc_29 = Button(frmc_6, bg=list_c[28], font=("", 36), command=fbtnc_29)
btnc_29.grid(row=0,column=3)
btnc_30 = Button(frmc_6, bg=list_c[29], font=("", 36), command=fbtnc_30)
btnc_30.grid(row=0,column=4)



frmc_7 = Frame(big_frm)
frmc_7.grid(row=1, column=1)

btnc_31 = Button(frmc_7, bg=list_c[30], font=("", 36), command=fbtnc_31)
btnc_31.grid(row=0,column=0)
btnc_32 = Button(frmc_7, bg=list_c[31], font=("", 36), command=fbtnc_32)
btnc_32.grid(row=0,column=1)
btnc_33 = Button(frmc_7, bg=list_c[32], font=("", 36), command=fbtnc_33)
btnc_33.grid(row=0,column=2)
btnc_34 = Button(frmc_7, bg=list_c[33], font=("", 36), command=fbtnc_34)
btnc_34.grid(row=0,column=3)
btnc_35 = Button(frmc_7, bg=list_c[34], font=("", 36), command=fbtnc_35)
btnc_35.grid(row=0,column=4)



frmc_8 = Frame(big_frm)
frmc_8.grid(row=1, column=2, padx=20)

btnc_36 = Button(frmc_8, bg=list_c[35], font=("", 36), command=fbtnc_36)
btnc_36.grid(row=0,column=0)
btnc_37 = Button(frmc_8, bg=list_c[36], font=("", 36), command=fbtnc_37)
btnc_37.grid(row=0,column=1)
btnc_38 = Button(frmc_8, bg=list_c[37], font=("", 36), command=fbtnc_38)
btnc_38.grid(row=0,column=2)
btnc_39 = Button(frmc_8, bg=list_c[38], font=("", 36), command=fbtnc_39)
btnc_39.grid(row=0,column=3)
btnc_40 = Button(frmc_8, bg=list_c[39], font=("", 36), command=fbtnc_40)
btnc_40.grid(row=0,column=4)



frmc_9 = Frame(big_frm)
frmc_9.grid(row=1, column=3)

btnc_41 = Button(frmc_9, bg=list_c[40], font=("", 36), command=fbtnc_41)
btnc_41.grid(row=0,column=0)
btnc_42 = Button(frmc_9, bg=list_c[41], font=("", 36), command=fbtnc_42)
btnc_42.grid(row=0,column=1)
btnc_43 = Button(frmc_9, bg=list_c[42], font=("", 36), command=fbtnc_43)
btnc_43.grid(row=0,column=2)
btnc_44 = Button(frmc_9, bg=list_c[43], font=("", 36), command=fbtnc_44)
btnc_44.grid(row=0,column=3)
btnc_45 = Button(frmc_9, bg=list_c[44], font=("", 36), command=fbtnc_45)
btnc_45.grid(row=0,column=4)



frmc_10 = Frame(big_frm)
frmc_10.grid(row=1, column=4, padx=20)

btnc_46 = Button(frmc_10, bg=list_c[45], font=("", 36), command=fbtnc_46)
btnc_46.grid(row=0,column=0)
btnc_47 = Button(frmc_10, bg=list_c[46], font=("", 36), command=fbtnc_47)
btnc_47.grid(row=0,column=1)
btnc_48 = Button(frmc_10, bg=list_c[47], font=("", 36), command=fbtnc_48)
btnc_48.grid(row=0,column=2)
btnc_49 = Button(frmc_10, bg=list_c[48], font=("", 36), command=fbtnc_49)
btnc_49.grid(row=0,column=3)
btnc_50 = Button(frmc_10, bg=list_c[49], font=("", 36), command=fbtnc_50)
btnc_50.grid(row=0,column=4)



frmc_11 = Frame(big_frm)
frmc_11.grid(row=2, column=0, padx=20)

btnc_51 = Button(frmc_11, bg=list_c[50], font=("", 36), command=fbtnc_51)
btnc_51.grid(row=0,column=0)
btnc_52 = Button(frmc_11, bg=list_c[51], font=("", 36), command=fbtnc_52)
btnc_52.grid(row=0,column=1)
btnc_53 = Button(frmc_11, bg=list_c[52], font=("", 36), command=fbtnc_53)
btnc_53.grid(row=0,column=2)
btnc_54 = Button(frmc_11, bg=list_c[53], font=("", 36), command=fbtnc_54)
btnc_54.grid(row=0,column=3)
btnc_55 = Button(frmc_11, bg=list_c[54], font=("", 36), command=fbtnc_55)
btnc_55.grid(row=0,column=4)

frmc_12 = Frame(big_frm)
frmc_12.grid(row=2, column=1)

btnc_56 = Button(frmc_12, bg=list_c[55], font=("", 36), command=fbtnc_56)
btnc_56.grid(row=0,column=0)
btnc_57 = Button(frmc_12, bg=list_c[56], font=("", 36), command=fbtnc_57)
btnc_57.grid(row=0,column=1)
btnc_58 = Button(frmc_12, bg=list_c[57], font=("", 36), command=fbtnc_58)
btnc_58.grid(row=0,column=2)
btnc_59 = Button(frmc_12, bg=list_c[58], font=("", 36), command=fbtnc_59)
btnc_59.grid(row=0,column=3)
btnc_60 = Button(frmc_12, bg=list_c[59], font=("", 36), command=fbtnc_60)
btnc_60.grid(row=0,column=4)


frmc_13 = Frame(big_frm)
frmc_13.grid(row=2, column=2, padx=20)

btnc_61 = Button(frmc_13, bg=list_c[60], font=("", 36), command=fbtnc_61)
btnc_61.grid(row=0,column=0)
btnc_62 = Button(frmc_13, bg=list_c[61], font=("", 36), command=fbtnc_62)
btnc_62.grid(row=0,column=1)
btnc_63 = Button(frmc_13, bg=list_c[62], font=("", 36), command=fbtnc_63)
btnc_63.grid(row=0,column=2)
btnc_64 = Button(frmc_13, bg=list_c[63], font=("", 36), command=fbtnc_64)
btnc_64.grid(row=0,column=3)
btnc_65 = Button(frmc_13, bg=list_c[64], font=("", 36), command=fbtnc_65)
btnc_65.grid(row=0,column=4)

frmc_14 = Frame(big_frm)
frmc_14.grid(row=2, column=3)

btnc_66 = Button(frmc_14, bg=list_c[65], font=("", 36), command=fbtnc_66)
btnc_66.grid(row=0,column=0)
btnc_67 = Button(frmc_14, bg=list_c[66], font=("", 36), command=fbtnc_67)
btnc_67.grid(row=0,column=1)
btnc_68 = Button(frmc_14, bg=list_c[67], font=("", 36), command=fbtnc_68)
btnc_68.grid(row=0,column=2)
btnc_69 = Button(frmc_14, bg=list_c[68], font=("", 36), command=fbtnc_69)
btnc_69.grid(row=0,column=3)
btnc_70 = Button(frmc_14, bg=list_c[69], font=("", 36), command=fbtnc_70)
btnc_70.grid(row=0,column=4)

frmc_15 = Frame(big_frm)
frmc_15.grid(row=2, column=4, padx=20, pady=20)

btnc_71 = Button(frmc_15, bg=list_c[70], font=("", 36), command=fbtnc_71)
btnc_71.grid(row=0,column=0)
btnc_72 = Button(frmc_15, bg=list_c[71], font=("", 36), command=fbtnc_72)
btnc_72.grid(row=0,column=1)
btnc_73 = Button(frmc_15, bg=list_c[72], font=("", 36), command=fbtnc_73)
btnc_73.grid(row=0,column=2)
btnc_74 = Button(frmc_15, bg=list_c[73], font=("", 36), command=fbtnc_74)
btnc_74.grid(row=0,column=3)
btnc_75 = Button(frmc_15, bg=list_c[74], font=("", 36), command=fbtnc_75)
btnc_75.grid(row=0,column=4)

frmc_16 = Frame(big_frm)
frmc_16.grid(row=3, column=0, padx=20)

btnc_76 = Button(frmc_16, bg=list_c[75], font=("", 36), command=fbtnc_76)
btnc_76.grid(row=0,column=0)
btnc_77 = Button(frmc_16, bg=list_c[76], font=("", 36), command=fbtnc_77)
btnc_77.grid(row=0,column=1)
btnc_78 = Button(frmc_16, bg=list_c[77], font=("", 36), command=fbtnc_78)
btnc_78.grid(row=0,column=2)
btnc_79 = Button(frmc_16, bg=list_c[78], font=("", 36), command=fbtnc_79)
btnc_79.grid(row=0,column=3)
btnc_80 = Button(frmc_16, bg=list_c[79], font=("", 36), command=fbtnc_80)
btnc_80.grid(row=0,column=4)

frmc_17 = Frame(big_frm)
frmc_17.grid(row=3, column=1)

btnc_81 = Button(frmc_17, bg=list_c[80], font=("", 36), command=fbtnc_81)
btnc_81.grid(row=0,column=0)
btnc_82 = Button(frmc_17, bg=list_c[81], font=("", 36), command=fbtnc_82)
btnc_82.grid(row=0,column=1)
btnc_83 = Button(frmc_17, bg=list_c[82], font=("", 36), command=fbtnc_83)
btnc_83.grid(row=0,column=2)
btnc_84 = Button(frmc_17, bg=list_c[83], font=("", 36), command=fbtnc_84)
btnc_84.grid(row=0,column=3)
btnc_85 = Button(frmc_17, bg=list_c[84], font=("", 36), command=fbtnc_85)
btnc_85.grid(row=0,column=4)

frmc_18 = Frame(big_frm)
frmc_18.grid(row=3, column=2, padx=20)

btnc_86 = Button(frmc_18, bg=list_c[85], font=("", 36), command=fbtnc_86)
btnc_86.grid(row=0,column=0)
btnc_87 = Button(frmc_18, bg=list_c[86], font=("", 36), command=fbtnc_87)
btnc_87.grid(row=0,column=1)
btnc_88 = Button(frmc_18, bg=list_c[87], font=("", 36), command=fbtnc_88)
btnc_88.grid(row=0,column=2)
btnc_89 = Button(frmc_18, bg=list_c[88], font=("", 36), command=fbtnc_89)
btnc_89.grid(row=0,column=3)
btnc_90 = Button(frmc_18, bg=list_c[89], font=("", 36), command=fbtnc_90)
btnc_90.grid(row=0,column=4)

frmc_19 = Frame(big_frm)
frmc_19.grid(row=3, column=3)

btnc_91 = Button(frmc_19, bg=list_c[90], font=("", 36), command=fbtnc_91)
btnc_91.grid(row=0,column=0)
btnc_92 = Button(frmc_19, bg=list_c[91], font=("", 36), command=fbtnc_92)
btnc_92.grid(row=0,column=1)
btnc_93 = Button(frmc_19, bg=list_c[92], font=("", 36), command=fbtnc_93)
btnc_93.grid(row=0,column=2)
btnc_94 = Button(frmc_19, bg=list_c[93], font=("", 36), command=fbtnc_94)
btnc_94.grid(row=0,column=3)
btnc_95 = Button(frmc_19, bg=list_c[94], font=("", 36), command=fbtnc_95)
btnc_95.grid(row=0,column=4)

frmc_20 = Frame(big_frm)
frmc_20.grid(row=3, column=4, padx=20)

btnc_96 = Button(frmc_20, bg=list_c[95], font=("", 36), command=fbtnc_96)
btnc_96.grid(row=0,column=0)
btnc_97 = Button(frmc_20, bg=list_c[96], font=("", 36), command=fbtnc_97)
btnc_97.grid(row=0,column=1)
btnc_98 = Button(frmc_20, bg=list_c[97], font=("", 36), command=fbtnc_98)
btnc_98.grid(row=0,column=2)
btnc_99 = Button(frmc_20, bg=list_c[98], font=("", 36), command=fbtnc_99)
btnc_99.grid(row=0,column=3)
btnc_100 = Button(frmc_20, bg=list_c[99], font=("", 36), command=fbtnc_100)
btnc_100.grid(row=0,column=4)

frmc_21 = Frame(big_frm)
frmc_21.grid(row=4, column=0, padx=20)

btnc_101 = Button(frmc_21, bg=list_c[100], font=("", 36), command=fbtnc_101)
btnc_101.grid(row=0,column=0)
btnc_102 = Button(frmc_21, bg=list_c[101], font=("", 36), command=fbtnc_102)
btnc_102.grid(row=0,column=1)
btnc_103 = Button(frmc_21, bg=list_c[102], font=("", 36), command=fbtnc_103)
btnc_103.grid(row=0,column=2)
btnc_104 = Button(frmc_21, bg=list_c[103], font=("", 36), command=fbtnc_104)
btnc_104.grid(row=0,column=3)
btnc_105 = Button(frmc_21, bg=list_c[104], font=("", 36), command=fbtnc_105)
btnc_105.grid(row=0,column=4)

frmc_22 = Frame(big_frm)
frmc_22.grid(row=4, column=1)

btnc_106 = Button(frmc_22, bg=list_c[105], font=("", 36), command=fbtnc_106)
btnc_106.grid(row=0,column=0)
btnc_107 = Button(frmc_22, bg=list_c[106], font=("", 36), command=fbtnc_107)
btnc_107.grid(row=0,column=1)
btnc_108 = Button(frmc_22, bg=list_c[107], font=("", 36), command=fbtnc_108)
btnc_108.grid(row=0,column=2)
btnc_109 = Button(frmc_22, bg=list_c[108], font=("", 36), command=fbtnc_109)
btnc_109.grid(row=0,column=3)
btnc_110 = Button(frmc_22, bg=list_c[109], font=("", 36), command=fbtnc_100)
btnc_110.grid(row=0,column=4)

frmc_23 = Frame(big_frm)
frmc_23.grid(row=4, column=2, padx=20)

btnc_111 = Button(frmc_23, bg=list_c[110], font=("", 36), command=fbtnc_111)
btnc_111.grid(row=0,column=0)
btnc_112 = Button(frmc_23, bg=list_c[111], font=("", 36), command=fbtnc_112)
btnc_112.grid(row=0,column=1)
btnc_113 = Button(frmc_23, bg=list_c[112], font=("", 36), command=fbtnc_113)
btnc_113.grid(row=0,column=2)
btnc_114 = Button(frmc_23, bg=list_c[113], font=("", 36), command=fbtnc_114)
btnc_114.grid(row=0,column=3)
btnc_115 = Button(frmc_23, bg=list_c[114], font=("", 36), command=fbtnc_115)
btnc_115.grid(row=0,column=4)

frmc_24 = Frame(big_frm)
frmc_24.grid(row=4, column=3)

btnc_116 = Button(frmc_24, bg=list_c[115], font=("", 36), command=fbtnc_116)
btnc_116.grid(row=0,column=0)
btnc_117 = Button(frmc_24, bg=list_c[116], font=("", 36), command=fbtnc_117)
btnc_117.grid(row=0,column=1)
btnc_118 = Button(frmc_24, bg=list_c[117], font=("", 36), command=fbtnc_118)
btnc_118.grid(row=0,column=2)
btnc_119 = Button(frmc_24, bg=list_c[118], font=("", 36), command=fbtnc_119)
btnc_119.grid(row=0,column=3)
btnc_120 = Button(frmc_24, bg=list_c[119], font=("", 36), command=fbtnc_120)
btnc_120.grid(row=0,column=4)


frmc_25 = Frame(big_frm)
frmc_25.grid(row=4, column=4, padx=20, pady=20)

btnc_121 = Button(frmc_25, bg=list_c[120], font=("", 36), command=fbtnc_121)
btnc_121.grid(row=0,column=0)
btnc_122 = Button(frmc_25, bg=list_c[121], font=("", 36), command=fbtnc_122)
btnc_122.grid(row=0,column=1)
btnc_123 = Button(frmc_25, bg=list_c[122], font=("", 36), command=fbtnc_123)
btnc_123.grid(row=0,column=2)
btnc_124 = Button(frmc_25, bg=list_c[123], font=("", 36), command=fbtnc_124)
btnc_124.grid(row=0,column=3)
btnc_125 = Button(frmc_25, bg=list_c[124], font=("", 36), command=fbtnc_125)
btnc_125.grid(row=0,column=4)



#---------------------------------------------------------------------------------------------------------------------



big_frm2 = Frame(root, bg="#f15bb5")

frmc_26 = Frame(big_frm2)
frmc_26.grid(row=0, column=0, padx=20)

btnc_126 = Button(frmc_26, bg=list_c[125], font=("", 36), command=fbtnc_126)
btnc_126.grid(row=0,column=0)
btnc_127 = Button(frmc_26, bg=list_c[126], font=("", 36), command=fbtnc_127)
btnc_127.grid(row=0,column=1)
btnc_128 = Button(frmc_26, bg=list_c[127], font=("", 36), command=fbtnc_128)
btnc_128.grid(row=0,column=2)
btnc_129 = Button(frmc_26, bg=list_c[128], font=("", 36), command=fbtnc_129)
btnc_129.grid(row=0,column=3)
btnc_130 = Button(frmc_26, bg=list_c[129], font=("", 36), command=fbtnc_130)
btnc_130.grid(row=0,column=4)

frmc_27 = Frame(big_frm2)
frmc_27.grid(row=0, column=1)

btnc_131 = Button(frmc_27, bg=list_c[130], font=("", 36), command=fbtnc_131)
btnc_131.grid(row=0,column=0)
btnc_132 = Button(frmc_27, bg=list_c[131], font=("", 36), command=fbtnc_132)
btnc_132.grid(row=0,column=1)
btnc_133 = Button(frmc_27, bg=list_c[132], font=("", 36), command=fbtnc_133)
btnc_133.grid(row=0,column=2)
btnc_134 = Button(frmc_27, bg=list_c[133], font=("", 36), command=fbtnc_134)
btnc_134.grid(row=0,column=3)
btnc_135 = Button(frmc_27, bg=list_c[134], font=("", 36), command=fbtnc_135)
btnc_135.grid(row=0,column=4)

frmc_28 = Frame(big_frm2)
frmc_28.grid(row=0, column=2, padx=20)

btnc_136 = Button(frmc_28, bg=list_c[135], font=("", 36), command=fbtnc_136)
btnc_136.grid(row=0,column=0)
btnc_137 = Button(frmc_28, bg=list_c[136], font=("", 36), command=fbtnc_137)
btnc_137.grid(row=0,column=1)
btnc_138 = Button(frmc_28, bg=list_c[137], font=("", 36), command=fbtnc_138)
btnc_138.grid(row=0,column=2)
btnc_139 = Button(frmc_28, bg=list_c[138], font=("", 36), command=fbtnc_139)
btnc_139.grid(row=0,column=3)
btnc_140 = Button(frmc_28, bg=list_c[139], font=("", 36), command=fbtnc_140)
btnc_140.grid(row=0,column=4)

frmc_29 = Frame(big_frm2)
frmc_29.grid(row=0, column=3, )

btnc_141 = Button(frmc_29, bg=list_c[140], font=("", 36), command=fbtnc_141)
btnc_141.grid(row=0,column=0)
btnc_142 = Button(frmc_29, bg=list_c[141], font=("", 36), command=fbtnc_142)
btnc_142.grid(row=0,column=1)
btnc_143 = Button(frmc_29, bg=list_c[142], font=("", 36), command=fbtnc_143)
btnc_143.grid(row=0,column=2)
btnc_144 = Button(frmc_29, bg=list_c[143], font=("", 36), command=fbtnc_144)
btnc_144.grid(row=0,column=3)
btnc_145 = Button(frmc_29, bg=list_c[144], font=("", 36), command=fbtnc_145)
btnc_145.grid(row=0,column=4)

frmc_30 = Frame(big_frm2)
frmc_30.grid(row=0, column=4, padx=20, pady=20)

btnc_146 = Button(frmc_30, bg=list_c[145], font=("", 36), command=fbtnc_146)
btnc_146.grid(row=0,column=0)
btnc_147 = Button(frmc_30, bg=list_c[146], font=("", 36), command=fbtnc_147)
btnc_147.grid(row=0,column=1)
btnc_148 = Button(frmc_30, bg=list_c[147], font=("", 36), command=fbtnc_148)
btnc_148.grid(row=0,column=2)
btnc_149 = Button(frmc_30, bg=list_c[148], font=("", 36), command=fbtnc_149)
btnc_149.grid(row=0,column=3)
btnc_150 = Button(frmc_30, bg=list_c[149], font=("", 36), command=fbtnc_150)
btnc_150.grid(row=0,column=4)

frmc_31 = Frame(big_frm2)
frmc_31.grid(row=1, column=0, padx=20)

btnc_151 = Button(frmc_31, bg=list_c[150], font=("", 36), command=fbtnc_151)
btnc_151.grid(row=0,column=0)
btnc_152 = Button(frmc_31, bg=list_c[151], font=("", 36), command=fbtnc_152)
btnc_152.grid(row=0,column=1)
btnc_153 = Button(frmc_31, bg=list_c[152], font=("", 36), command=fbtnc_153)
btnc_153.grid(row=0,column=2)
btnc_154 = Button(frmc_31, bg=list_c[153], font=("", 36), command=fbtnc_154)
btnc_154.grid(row=0,column=3)
btnc_155 = Button(frmc_31, bg=list_c[154], font=("", 36), command=fbtnc_155)
btnc_155.grid(row=0,column=4)

frmc_32 = Frame(big_frm2)
frmc_32.grid(row=1, column=1)

btnc_156 = Button(frmc_32, bg=list_c[155], font=("", 36), command=fbtnc_156)
btnc_156.grid(row=0,column=0)
btnc_157 = Button(frmc_32, bg=list_c[156], font=("", 36), command=fbtnc_157)
btnc_157.grid(row=0,column=1)
btnc_158 = Button(frmc_32, bg=list_c[157], font=("", 36), command=fbtnc_158)
btnc_158.grid(row=0,column=2)
btnc_159 = Button(frmc_32, bg=list_c[158], font=("", 36), command=fbtnc_159)
btnc_159.grid(row=0,column=3)
btnc_160 = Button(frmc_32, bg=list_c[159], font=("", 36), command=fbtnc_160)
btnc_160.grid(row=0,column=4)

frmc_33 = Frame(big_frm2)
frmc_33.grid(row=1, column=2, padx=20)

btnc_161 = Button(frmc_33, bg=list_c[160], font=("", 36), command=fbtnc_161)
btnc_161.grid(row=0,column=0)
btnc_162 = Button(frmc_33, bg=list_c[161], font=("", 36), command=fbtnc_162)
btnc_162.grid(row=0,column=1)
btnc_163 = Button(frmc_33, bg=list_c[162], font=("", 36), command=fbtnc_163)
btnc_163.grid(row=0,column=2)
btnc_164 = Button(frmc_33, bg=list_c[163], font=("", 36), command=fbtnc_164)
btnc_164.grid(row=0,column=3)
btnc_165 = Button(frmc_33, bg=list_c[164], font=("", 36), command=fbtnc_165)
btnc_165.grid(row=0,column=4)

frmc_34 = Frame(big_frm2)
frmc_34.grid(row=1, column=3)

btnc_166 = Button(frmc_34, bg=list_c[165], font=("", 36), command=fbtnc_166)
btnc_166.grid(row=0,column=0)
btnc_167 = Button(frmc_34, bg=list_c[166], font=("", 36), command=fbtnc_167)
btnc_167.grid(row=0,column=1)
btnc_168 = Button(frmc_34, bg=list_c[167], font=("", 36), command=fbtnc_168)
btnc_168.grid(row=0,column=2)
btnc_169 = Button(frmc_34, bg=list_c[168], font=("", 36), command=fbtnc_169)
btnc_169.grid(row=0,column=3)
btnc_170 = Button(frmc_34, bg=list_c[169], font=("", 36), command=fbtnc_170)
btnc_170.grid(row=0,column=4)

frmc_35 = Frame(big_frm2)
frmc_35.grid(row=1, column=4, padx=20)

btnc_171 = Button(frmc_35, bg=list_c[170], font=("", 36), command=fbtnc_171)
btnc_171.grid(row=0,column=0)
btnc_172 = Button(frmc_35, bg=list_c[171], font=("", 36), command=fbtnc_172)
btnc_172.grid(row=0,column=1)
btnc_173 = Button(frmc_35, bg=list_c[172], font=("", 36), command=fbtnc_173)
btnc_173.grid(row=0,column=2)
btnc_174 = Button(frmc_35, bg=list_c[173], font=("", 36), command=fbtnc_174)
btnc_174.grid(row=0,column=3)
btnc_175 = Button(frmc_35, bg=list_c[174], font=("", 36), command=fbtnc_175)
btnc_175.grid(row=0,column=4)

frmc_36 = Frame(big_frm2)
frmc_36.grid(row=2, column=0, padx=20)

btnc_176 = Button(frmc_36, bg=list_c[175], font=("", 36), command=fbtnc_176)
btnc_176.grid(row=0,column=0)
btnc_177 = Button(frmc_36, bg=list_c[176], font=("", 36), command=fbtnc_177)
btnc_177.grid(row=0,column=1)
btnc_178 = Button(frmc_36, bg=list_c[177], font=("", 36), command=fbtnc_178)
btnc_178.grid(row=0,column=2)
btnc_179 = Button(frmc_36, bg=list_c[178], font=("", 36), command=fbtnc_179)
btnc_179.grid(row=0,column=3)
btnc_180 = Button(frmc_36, bg=list_c[179], font=("", 36), command=fbtnc_180)
btnc_180.grid(row=0,column=4)

frmc_37 = Frame(big_frm2)
frmc_37.grid(row=2, column=1)

btnc_181 = Button(frmc_37, bg=list_c[180], font=("", 36), command=fbtnc_181)
btnc_181.grid(row=0,column=0)
btnc_182 = Button(frmc_37, bg=list_c[181], font=("", 36), command=fbtnc_182)
btnc_182.grid(row=0,column=1)
btnc_183 = Button(frmc_37, bg=list_c[182], font=("", 36), command=fbtnc_183)
btnc_183.grid(row=0,column=2)
btnc_184 = Button(frmc_37, bg=list_c[183], font=("", 36), command=fbtnc_184)
btnc_184.grid(row=0,column=3)
btnc_185 = Button(frmc_37, bg=list_c[184], font=("", 36), command=fbtnc_185)
btnc_185.grid(row=0,column=4)

frmc_38 = Frame(big_frm2)
frmc_38.grid(row=2, column=2, padx=20)

btnc_186 = Button(frmc_38, bg=list_c[185], font=("", 36), command=fbtnc_186)
btnc_186.grid(row=0,column=0)
btnc_187 = Button(frmc_38, bg=list_c[186], font=("", 36), command=fbtnc_187)
btnc_187.grid(row=0,column=1)
btnc_188 = Button(frmc_38, bg=list_c[187], font=("", 36), command=fbtnc_188)
btnc_188.grid(row=0,column=2)
btnc_189 = Button(frmc_38, bg=list_c[188], font=("", 36), command=fbtnc_189)
btnc_189.grid(row=0,column=3)
btnc_190 = Button(frmc_38, bg=list_c[189], font=("", 36), command=fbtnc_190)
btnc_190.grid(row=0,column=4)

frmc_39 = Frame(big_frm2)
frmc_39.grid(row=2, column=3)

btnc_191 = Button(frmc_39, bg=list_c[190], font=("", 36), command=fbtnc_191)
btnc_191.grid(row=0,column=0)
btnc_192 = Button(frmc_39, bg=list_c[191], font=("", 36), command=fbtnc_192)
btnc_192.grid(row=0,column=1)
btnc_193 = Button(frmc_39, bg=list_c[192], font=("", 36), command=fbtnc_193)
btnc_193.grid(row=0,column=2)
btnc_194 = Button(frmc_39, bg=list_c[193], font=("", 36), command=fbtnc_194)
btnc_194.grid(row=0,column=3)
btnc_195 = Button(frmc_39, bg=list_c[194], font=("", 36), command=fbtnc_195)
btnc_195.grid(row=0,column=4)


frmc_40 = Frame(big_frm2)
frmc_40.grid(row=2, column=4, padx=20, pady=20)

btnc_196 = Button(frmc_40, bg=list_c[195], font=("", 36), command=fbtnc_196)
btnc_196.grid(row=0,column=0)
btnc_197 = Button(frmc_40, bg=list_c[196], font=("", 36), command=fbtnc_197)
btnc_197.grid(row=0,column=1)
btnc_198 = Button(frmc_40, bg=list_c[197], font=("", 36), command=fbtnc_198)
btnc_198.grid(row=0,column=2)
btnc_199 = Button(frmc_40, bg=list_c[198], font=("", 36), command=fbtnc_199)
btnc_199.grid(row=0,column=3)
btnc_200 = Button(frmc_40, bg=list_c[199], font=("", 36), command=fbtnc_200)
btnc_200.grid(row=0,column=4)

frmc_41 = Frame(big_frm2)
frmc_41.grid(row=3, column=0, padx=20)

btnc_201 = Button(frmc_41, bg=list_c[200], font=("", 36), command=fbtnc_201)
btnc_201.grid(row=0,column=0)
btnc_202 = Button(frmc_41, bg=list_c[201], font=("", 36), command=fbtnc_202)
btnc_202.grid(row=0,column=1)
btnc_203 = Button(frmc_41, bg=list_c[202], font=("", 36), command=fbtnc_203)
btnc_203.grid(row=0,column=2)
btnc_204 = Button(frmc_41, bg=list_c[203], font=("", 36), command=fbtnc_204)
btnc_204.grid(row=0,column=3)
btnc_205 = Button(frmc_41, bg=list_c[204], font=("", 36), command=fbtnc_205)
btnc_205.grid(row=0,column=4)

frmc_42 = Frame(big_frm2)
frmc_42.grid(row=3, column=1)

btnc_206 = Button(frmc_42, bg=list_c[205], font=("", 36), command=fbtnc_206)
btnc_206.grid(row=0,column=0)
btnc_207 = Button(frmc_42, bg=list_c[206], font=("", 36), command=fbtnc_207)
btnc_207.grid(row=0,column=1)
btnc_208 = Button(frmc_42, bg=list_c[207], font=("", 36), command=fbtnc_208)
btnc_208.grid(row=0,column=2)
btnc_209 = Button(frmc_42, bg=list_c[208], font=("", 36), command=fbtnc_209)
btnc_209.grid(row=0,column=3)
btnc_210 = Button(frmc_42, bg=list_c[209], font=("", 36), command=fbtnc_210)
btnc_210.grid(row=0,column=4)


frmc_43 = Frame(big_frm2)
frmc_43.grid(row=3, column=2, padx=20)

btnc_211 = Button(frmc_43, bg=list_c[210], font=("", 36), command=fbtnc_211)
btnc_211.grid(row=0,column=0)
btnc_212 = Button(frmc_43, bg=list_c[211], font=("", 36), command=fbtnc_212)
btnc_212.grid(row=0,column=1)
btnc_213 = Button(frmc_43, bg=list_c[212], font=("", 36), command=fbtnc_213)
btnc_213.grid(row=0,column=2)
btnc_214 = Button(frmc_43, bg=list_c[213], font=("", 36), command=fbtnc_214)
btnc_214.grid(row=0,column=3)
btnc_215 = Button(frmc_43, bg=list_c[214], font=("", 36), command=fbtnc_215)
btnc_215.grid(row=0,column=4)

frmc_44 = Frame(big_frm2)
frmc_44.grid(row=3, column=3)

btnc_216 = Button(frmc_44, bg=list_c[215], font=("", 36), command=fbtnc_206)
btnc_216.grid(row=0,column=0)
btnc_217 = Button(frmc_44, bg=list_c[216], font=("", 36), command=fbtnc_217)
btnc_217.grid(row=0,column=1)
btnc_218 = Button(frmc_44, bg=list_c[217], font=("", 36), command=fbtnc_218)
btnc_218.grid(row=0,column=2)
btnc_219 = Button(frmc_44, bg=list_c[218], font=("", 36), command=fbtnc_219)
btnc_219.grid(row=0,column=3)
btnc_220 = Button(frmc_44, bg=list_c[219], font=("", 36), command=fbtnc_220)
btnc_220.grid(row=0,column=4)


frmc_45 = Frame(big_frm2)
frmc_45.grid(row=3, column=4, padx=20)

btnc_221 = Button(frmc_45, bg=list_c[220], font=("", 36), command=fbtnc_221)
btnc_221.grid(row=0,column=0)
btnc_222 = Button(frmc_45, bg=list_c[221], font=("", 36), command=fbtnc_222)
btnc_222.grid(row=0,column=1)
btnc_223 = Button(frmc_45, bg=list_c[222], font=("", 36), command=fbtnc_223)
btnc_223.grid(row=0,column=2)
btnc_224 = Button(frmc_45, bg=list_c[223], font=("", 36), command=fbtnc_224)
btnc_224.grid(row=0,column=3)
btnc_225 = Button(frmc_45, bg=list_c[224], font=("", 36), command=fbtnc_225)
btnc_225.grid(row=0,column=4)

frmc_46 = Frame(big_frm2)
frmc_46.grid(row=4, column=0, padx=20)
btnc_226 = Button(frmc_46, bg=list_c[225], font=("", 36), command=fbtnc_226)
btnc_226.grid(row=0,column=0)
btnc_227 = Button(frmc_46, bg=list_c[226], font=("", 36), command=fbtnc_227)
btnc_227.grid(row=0,column=1)
btnc_228 = Button(frmc_46, bg=list_c[227], font=("", 36), command=fbtnc_228)
btnc_228.grid(row=0,column=2)
btnc_229 = Button(frmc_46, bg=list_c[228], font=("", 36), command=fbtnc_229)
btnc_229.grid(row=0,column=3)
btnc_230 = Button(frmc_46, bg=list_c[229], font=("", 36), command=fbtnc_230)
btnc_230.grid(row=0,column=4)

frmc_47 = Frame(big_frm2)
frmc_47.grid(row=4, column=1)

btnc_231 = Button(frmc_47, bg=list_c[230], font=("", 36), command=fbtnc_231)
btnc_231.grid(row=0,column=0)
btnc_232 = Button(frmc_47, bg=list_c[231], font=("", 36), command=fbtnc_232)
btnc_232.grid(row=0,column=1)
btnc_233 = Button(frmc_47, bg=list_c[232], font=("", 36), command=fbtnc_233)
btnc_233.grid(row=0,column=2)
btnc_234 = Button(frmc_47, bg=list_c[233], font=("", 36), command=fbtnc_234)
btnc_234.grid(row=0,column=3)
btnc_235 = Button(frmc_47, bg=list_c[234], font=("", 36), command=fbtnc_235)
btnc_235.grid(row=0,column=4)

frmc_48 = Frame(big_frm2)
frmc_48.grid(row=4, column=2, padx=20)

btnc_236 = Button(frmc_48, bg=list_c[235], font=("", 36), command=fbtnc_236)
btnc_236.grid(row=0,column=0)
btnc_237 = Button(frmc_48, bg=list_c[236], font=("", 36), command=fbtnc_237)
btnc_237.grid(row=0,column=1)
btnc_238 = Button(frmc_48, bg=list_c[237], font=("", 36), command=fbtnc_238)
btnc_238.grid(row=0,column=2)
btnc_239 = Button(frmc_48, bg=list_c[238], font=("", 36), command=fbtnc_239)
btnc_239.grid(row=0,column=3)
btnc_240 = Button(frmc_48, bg=list_c[239], font=("", 36), command=fbtnc_240)
btnc_240.grid(row=0,column=4)

frmc_49 = Frame(big_frm2)
frmc_49.grid(row=4, column=3)

btnc_241 = Button(frmc_49, bg=list_c[240], font=("", 36), command=fbtnc_241)
btnc_241.grid(row=0,column=0)
btnc_242 = Button(frmc_49, bg=list_c[241], font=("", 36), command=fbtnc_242)
btnc_242.grid(row=0,column=1)
btnc_243 = Button(frmc_49, bg=list_c[242], font=("", 36), command=fbtnc_243)
btnc_243.grid(row=0,column=2)
btnc_244 = Button(frmc_49, bg=list_c[243], font=("", 36), command=fbtnc_244)
btnc_244.grid(row=0,column=3)
btnc_245 = Button(frmc_49, bg=list_c[244], font=("", 36), command=fbtnc_245)
btnc_245.grid(row=0,column=4)

frmc_50 = Frame(big_frm2)
frmc_50.grid(row=4, column=4, padx=20, pady=20)

btnc_246 = Button(frmc_50, bg=list_c[245], font=("", 36), command=fbtnc_246)
btnc_246.grid(row=0,column=0)
btnc_247 = Button(frmc_50, bg=list_c[246], font=("", 36), command=fbtnc_247)
btnc_247.grid(row=0,column=1)
btnc_248 = Button(frmc_50, bg=list_c[247], font=("", 36), command=fbtnc_248)
btnc_248.grid(row=0,column=2)
btnc_249 = Button(frmc_50, bg=list_c[248], font=("", 36), command=fbtnc_249)
btnc_249.grid(row=0,column=3)
btnc_250 = Button(frmc_50, bg=list_c[249], font=("", 36), command=fbtnc_250)
btnc_250.grid(row=0,column=4)



#-----------------------------------------------------------------------------------------------------------------------------



big_frm3 = Frame(root, bg="#f15bb5")

frmc_51 = Frame(big_frm3)
frmc_51.grid(row=0, column=0, padx=20)

btnc_251 = Button(frmc_51, bg=list_c[250], font=("", 36), command=fbtnc_251)
btnc_251.grid(row=0,column=0)
btnc_252 = Button(frmc_51, bg=list_c[251], font=("", 36), command=fbtnc_252)
btnc_252.grid(row=0,column=1)
btnc_253 = Button(frmc_51, bg=list_c[252], font=("", 36), command=fbtnc_253)
btnc_253.grid(row=0,column=2)
btnc_254 = Button(frmc_51, bg=list_c[253], font=("", 36), command=fbtnc_254)
btnc_254.grid(row=0,column=3)
btnc_255 = Button(frmc_51, bg=list_c[254], font=("", 36), command=fbtnc_255)
btnc_255.grid(row=0,column=4)

frmc_52 = Frame(big_frm3)
frmc_52.grid(row=0, column=1)

btnc_256 = Button(frmc_52, bg=list_c[255], font=("", 36), command=fbtnc_256)
btnc_256.grid(row=0,column=0)
btnc_257 = Button(frmc_52, bg=list_c[256], font=("", 36), command=fbtnc_257)
btnc_257.grid(row=0,column=1)
btnc_258 = Button(frmc_52, bg=list_c[257], font=("", 36), command=fbtnc_258)
btnc_258.grid(row=0,column=2)
btnc_259 = Button(frmc_52, bg=list_c[258], font=("", 36), command=fbtnc_259)
btnc_259.grid(row=0,column=3)
btnc_260 = Button(frmc_52, bg=list_c[259], font=("", 36), command=fbtnc_260)
btnc_260.grid(row=0,column=4)

frmc_53 = Frame(big_frm3)
frmc_53.grid(row=0, column=2, padx=20)

btnc_261 = Button(frmc_53, bg=list_c[260], font=("", 36), command=fbtnc_261)
btnc_261.grid(row=0,column=0)
btnc_262 = Button(frmc_53, bg=list_c[261], font=("", 36), command=fbtnc_262)
btnc_262.grid(row=0,column=1)
btnc_263 = Button(frmc_53, bg=list_c[262], font=("", 36), command=fbtnc_263)
btnc_263.grid(row=0,column=2)
btnc_264 = Button(frmc_53, bg=list_c[263], font=("", 36), command=fbtnc_264)
btnc_264.grid(row=0,column=3)
btnc_265 = Button(frmc_53, bg=list_c[264], font=("", 36), command=fbtnc_265)
btnc_265.grid(row=0,column=4)

frmc_54 = Frame(big_frm3)
frmc_54.grid(row=0, column=3)

btnc_266 = Button(frmc_54, bg=list_c[265], font=("", 36), command=fbtnc_266)
btnc_266.grid(row=0,column=0)
btnc_267 = Button(frmc_54, bg=list_c[266], font=("", 36), command=fbtnc_267)
btnc_267.grid(row=0,column=1)
btnc_268 = Button(frmc_54, bg=list_c[267], font=("", 36), command=fbtnc_268)
btnc_268.grid(row=0,column=2)
btnc_269 = Button(frmc_54, bg=list_c[268], font=("", 36), command=fbtnc_269)
btnc_269.grid(row=0,column=3)
btnc_270 = Button(frmc_54, bg=list_c[269], font=("", 36), command=fbtnc_270)
btnc_270.grid(row=0,column=4)

frmc_55 = Frame(big_frm3)
frmc_55.grid(row=0, column=4, padx=20, pady=20)

btnc_271 = Button(frmc_55, bg=list_c[270], font=("", 36), command=fbtnc_271)
btnc_271.grid(row=0,column=0)
btnc_272 = Button(frmc_55, bg=list_c[271], font=("", 36), command=fbtnc_272)
btnc_272.grid(row=0,column=1)
btnc_273 = Button(frmc_55, bg=list_c[272], font=("", 36), command=fbtnc_273)
btnc_273.grid(row=0,column=2)
btnc_274 = Button(frmc_55, bg=list_c[273], font=("", 36), command=fbtnc_274)
btnc_274.grid(row=0,column=3)
btnc_275 = Button(frmc_55, bg=list_c[274], font=("", 36), command=fbtnc_275)
btnc_275.grid(row=0,column=4)

frmc_56 = Frame(big_frm3)
frmc_56.grid(row=1, column=0, padx=20)

btnc_276 = Button(frmc_56, bg=list_c[275], font=("", 36), command=fbtnc_276)
btnc_276.grid(row=0,column=0)
btnc_277 = Button(frmc_56, bg=list_c[276], font=("", 36), command=fbtnc_277)
btnc_277.grid(row=0,column=1)
btnc_278 = Button(frmc_56, bg=list_c[277], font=("", 36), command=fbtnc_278)
btnc_278.grid(row=0,column=2)
btnc_279 = Button(frmc_56, bg=list_c[278], font=("", 36), command=fbtnc_279)
btnc_279.grid(row=0,column=3)
btnc_280 = Button(frmc_56, bg=list_c[279], font=("", 36), command=fbtnc_270)
btnc_280.grid(row=0,column=4)


frmc_57 = Frame(big_frm3)
frmc_57.grid(row=1, column=1)

btnc_281 = Button(frmc_57, bg=list_c[280], font=("", 36), command=fbtnc_281)
btnc_281.grid(row=0,column=0)
btnc_282 = Button(frmc_57, bg=list_c[281], font=("", 36), command=fbtnc_282)
btnc_282.grid(row=0,column=1)
btnc_283 = Button(frmc_57, bg=list_c[282], font=("", 36), command=fbtnc_283)
btnc_283.grid(row=0,column=2)
btnc_284 = Button(frmc_57, bg=list_c[283], font=("", 36), command=fbtnc_284)
btnc_284.grid(row=0,column=3)
btnc_285 = Button(frmc_57, bg=list_c[284], font=("", 36), command=fbtnc_285)
btnc_285.grid(row=0,column=4)

frmc_58 = Frame(big_frm3)
frmc_58.grid(row=1, column=2, padx=20)

btnc_286 = Button(frmc_58, bg=list_c[285], font=("", 36), command=fbtnc_286)
btnc_286.grid(row=0,column=0)
btnc_287 = Button(frmc_58, bg=list_c[286], font=("", 36), command=fbtnc_287)
btnc_287.grid(row=0,column=1)
btnc_288 = Button(frmc_58, bg=list_c[287], font=("", 36), command=fbtnc_288)
btnc_288.grid(row=0,column=2)
btnc_289 = Button(frmc_58, bg=list_c[288], font=("", 36), command=fbtnc_289)
btnc_289.grid(row=0,column=3)
btnc_290 = Button(frmc_58, bg=list_c[289], font=("", 36), command=fbtnc_290)
btnc_290.grid(row=0,column=4)


frmc_59 = Frame(big_frm3)
frmc_59.grid(row=1, column=3)

btnc_291 = Button(frmc_59, bg=list_c[290], font=("", 36), command=fbtnc_291)
btnc_291.grid(row=0,column=0)
btnc_292 = Button(frmc_59, bg=list_c[291], font=("", 36), command=fbtnc_292)
btnc_292.grid(row=0,column=1)
btnc_293 = Button(frmc_59, bg=list_c[292], font=("", 36), command=fbtnc_293)
btnc_293.grid(row=0,column=2)
btnc_294 = Button(frmc_59, bg=list_c[293], font=("", 36), command=fbtnc_294)
btnc_294.grid(row=0,column=3)
btnc_295 = Button(frmc_59, bg=list_c[294], font=("", 36), command=fbtnc_295)
btnc_295.grid(row=0,column=4)

frmc_60 = Frame(big_frm3)
frmc_60.grid(row=1, column=4, padx=20)

btnc_296 = Button(frmc_60, bg=list_c[295], font=("", 36), command=fbtnc_296)
btnc_296.grid(row=0,column=0)
btnc_297 = Button(frmc_60, bg=list_c[296], font=("", 36), command=fbtnc_297)
btnc_297.grid(row=0,column=1)
btnc_298 = Button(frmc_60, bg=list_c[297], font=("", 36), command=fbtnc_298)
btnc_298.grid(row=0,column=2)
btnc_299 = Button(frmc_60, bg=list_c[298], font=("", 36), command=fbtnc_299)
btnc_299.grid(row=0,column=3)
btnc_300 = Button(frmc_60, bg=list_c[299], font=("", 36), command=fbtnc_300)
btnc_300.grid(row=0,column=4)

frmc_61 = Frame(big_frm3)
frmc_61.grid(row=2, column=0, padx=20)

btnc_301 = Button(frmc_61, bg=list_c[300], font=("", 36), command=fbtnc_301)
btnc_301.grid(row=0,column=0)
btnc_302 = Button(frmc_61, bg=list_c[301], font=("", 36), command=fbtnc_302)
btnc_302.grid(row=0,column=1)
btnc_303 = Button(frmc_61, bg=list_c[302], font=("", 36), command=fbtnc_303)
btnc_303.grid(row=0,column=2)
btnc_304 = Button(frmc_61, bg=list_c[303], font=("", 36), command=fbtnc_304)
btnc_304.grid(row=0,column=3)
btnc_305 = Button(frmc_61, bg=list_c[304], font=("", 36), command=fbtnc_305)
btnc_305.grid(row=0,column=4)

frmc_62 = Frame(big_frm3)
frmc_62.grid(row=2, column=1)

btnc_306 = Button(frmc_62, bg=list_c[305], font=("", 36), command=fbtnc_306)
btnc_306.grid(row=0,column=0)
btnc_307 = Button(frmc_62, bg=list_c[306], font=("", 36), command=fbtnc_307)
btnc_307.grid(row=0,column=1)
btnc_308 = Button(frmc_62, bg=list_c[307], font=("", 36), command=fbtnc_308)
btnc_308.grid(row=0,column=2)
btnc_309 = Button(frmc_62, bg=list_c[308], font=("", 36), command=fbtnc_309)
btnc_309.grid(row=0,column=3)
btnc_310 = Button(frmc_62, bg=list_c[309], font=("", 36), command=fbtnc_310)
btnc_310.grid(row=0,column=4)

frmc_63 = Frame(big_frm3)
frmc_63.grid(row=2, column=2, padx=20)

btnc_311 = Button(frmc_63, bg=list_c[310], font=("", 36), command=fbtnc_311)
btnc_311.grid(row=0,column=0)
btnc_312 = Button(frmc_63, bg=list_c[311], font=("", 36), command=fbtnc_312)
btnc_312.grid(row=0,column=1)
btnc_313 = Button(frmc_63, bg=list_c[312], font=("", 36), command=fbtnc_313)
btnc_313.grid(row=0,column=2)
btnc_314 = Button(frmc_63, bg=list_c[313], font=("", 36), command=fbtnc_314)
btnc_314.grid(row=0,column=3)
btnc_315 = Button(frmc_63, bg=list_c[314], font=("", 36), command=fbtnc_315)
btnc_315.grid(row=0,column=4)

frmc_64 = Frame(big_frm3)
frmc_64.grid(row=2, column=3)

btnc_316 = Button(frmc_64, bg=list_c[315], font=("", 36), command=fbtnc_316)
btnc_316.grid(row=0,column=0)
btnc_317 = Button(frmc_64, bg=list_c[316], font=("", 36), command=fbtnc_317)
btnc_317.grid(row=0,column=1)
btnc_318 = Button(frmc_64, bg=list_c[317], font=("", 36), command=fbtnc_318)
btnc_318.grid(row=0,column=2)
btnc_319 = Button(frmc_64, bg=list_c[318], font=("", 36), command=fbtnc_319)
btnc_319.grid(row=0,column=3)
btnc_320 = Button(frmc_64, bg=list_c[319], font=("", 36), command=fbtnc_320)
btnc_320.grid(row=0,column=4)

frmc_65 = Frame(big_frm3)
frmc_65.grid(row=2, column=4, padx=20, pady=20)

btnc_321 = Button(frmc_65, bg=list_c[320], font=("", 36), command=fbtnc_321)
btnc_321.grid(row=0,column=0)
btnc_322 = Button(frmc_65, bg=list_c[321], font=("", 36), command=fbtnc_322)
btnc_322.grid(row=0,column=1)
btnc_323 = Button(frmc_65, bg=list_c[322], font=("", 36), command=fbtnc_323)
btnc_323.grid(row=0,column=2)
btnc_324 = Button(frmc_65, bg=list_c[323], font=("", 36), command=fbtnc_324)
btnc_324.grid(row=0,column=3)
btnc_325 = Button(frmc_65, bg=list_c[324], font=("", 36), command=fbtnc_325)
btnc_325.grid(row=0,column=4)

frmc_66 = Frame(big_frm3)
frmc_66.grid(row=3, column=0, padx=20)

btnc_326 = Button(frmc_66, bg=list_c[325], font=("", 36), command=fbtnc_326)
btnc_326.grid(row=0,column=0)
btnc_327 = Button(frmc_66, bg=list_c[326], font=("", 36), command=fbtnc_327)
btnc_327.grid(row=0,column=1)
btnc_328 = Button(frmc_66, bg=list_c[327], font=("", 36), command=fbtnc_328)
btnc_328.grid(row=0,column=2)
btnc_329 = Button(frmc_66, bg=list_c[328], font=("", 36), command=fbtnc_329)
btnc_329.grid(row=0,column=3)
btnc_330 = Button(frmc_66, bg=list_c[329], font=("", 36), command=fbtnc_330)
btnc_330.grid(row=0,column=4)

frmc_67 = Frame(big_frm3)
frmc_67.grid(row=3, column=1)

btnc_331 = Button(frmc_67, bg=list_c[330], font=("", 36), command=fbtnc_331)
btnc_331.grid(row=0,column=0)
btnc_332 = Button(frmc_67, bg=list_c[331], font=("", 36), command=fbtnc_332)
btnc_332.grid(row=0,column=1)
btnc_333 = Button(frmc_67, bg=list_c[332], font=("", 36), command=fbtnc_333)
btnc_333.grid(row=0,column=2)
btnc_334 = Button(frmc_67, bg=list_c[333], font=("", 36), command=fbtnc_334)
btnc_334.grid(row=0,column=3)
btnc_335 = Button(frmc_67, bg=list_c[334], font=("", 36), command=fbtnc_335)
btnc_335.grid(row=0,column=4)

frmc_68 = Frame(big_frm3)
frmc_68.grid(row=3, column=2, padx=20)

btnc_336 = Button(frmc_68, bg=list_c[335], font=("", 36), command=fbtnc_336)
btnc_336.grid(row=0,column=0)
btnc_337 = Button(frmc_68, bg=list_c[336], font=("", 36), command=fbtnc_337)
btnc_337.grid(row=0,column=1)
btnc_338 = Button(frmc_68, bg=list_c[337], font=("", 36), command=fbtnc_338)
btnc_338.grid(row=0,column=2)
btnc_339 = Button(frmc_68, bg=list_c[338], font=("", 36), command=fbtnc_339)
btnc_339.grid(row=0,column=3)
btnc_340 = Button(frmc_68, bg=list_c[339], font=("", 36), command=fbtnc_340)
btnc_340.grid(row=0,column=4)

frmc_69 = Frame(big_frm3)
frmc_69.grid(row=3, column=3)

btnc_341 = Button(frmc_69, bg=list_c[340], font=("", 36), command=fbtnc_341)
btnc_341.grid(row=0,column=0)
btnc_342 = Button(frmc_69, bg=list_c[341], font=("", 36), command=fbtnc_342)
btnc_342.grid(row=0,column=1)
btnc_343 = Button(frmc_69, bg=list_c[342], font=("", 36), command=fbtnc_343)
btnc_343.grid(row=0,column=2)
btnc_344 = Button(frmc_69, bg=list_c[343], font=("", 36), command=fbtnc_344)
btnc_344.grid(row=0,column=3)
btnc_345 = Button(frmc_69, bg=list_c[344], font=("", 36), command=fbtnc_345)
btnc_345.grid(row=0,column=4)

frmc_70 = Frame(big_frm3)
frmc_70.grid(row=3, column=4, padx=20)

btnc_346 = Button(frmc_70, bg=list_c[345], font=("", 36), command=fbtnc_346)
btnc_346.grid(row=0,column=0)
btnc_347 = Button(frmc_70, bg=list_c[346], font=("", 36), command=fbtnc_347)
btnc_347.grid(row=0,column=1)
btnc_348 = Button(frmc_70, bg=list_c[347], font=("", 36), command=fbtnc_348)
btnc_348.grid(row=0,column=2)
btnc_349 = Button(frmc_70, bg=list_c[348], font=("", 36), command=fbtnc_349)
btnc_349.grid(row=0,column=3)
btnc_350 = Button(frmc_70, bg=list_c[349], font=("", 36), command=fbtnc_350)
btnc_350.grid(row=0,column=4)

frmc_71 = Frame(big_frm3)
frmc_71.grid(row=4, column=0, padx=20)

btnc_351 = Button(frmc_71, bg=list_c[350], font=("", 36), command=fbtnc_351)
btnc_351.grid(row=0,column=0)
btnc_352 = Button(frmc_71, bg=list_c[351], font=("", 36), command=fbtnc_352)
btnc_352.grid(row=0,column=1)
btnc_353 = Button(frmc_71, bg=list_c[352], font=("", 36), command=fbtnc_353)
btnc_353.grid(row=0,column=2)
btnc_354 = Button(frmc_71, bg=list_c[353], font=("", 36), command=fbtnc_354)
btnc_354.grid(row=0,column=3)
btnc_355 = Button(frmc_71, bg=list_c[354], font=("", 36), command=fbtnc_355)
btnc_355.grid(row=0,column=4)

frmc_72 = Frame(big_frm3)
frmc_72.grid(row=4, column=1)

btnc_356 = Button(frmc_72, bg=list_c[355], font=("", 36), command=fbtnc_356)
btnc_356.grid(row=0,column=0)
btnc_357 = Button(frmc_72, bg=list_c[356], font=("", 36), command=fbtnc_357)
btnc_357.grid(row=0,column=1)
btnc_358 = Button(frmc_72, bg=list_c[357], font=("", 36), command=fbtnc_358)
btnc_358.grid(row=0,column=2)
btnc_359 = Button(frmc_72, bg=list_c[358], font=("", 36), command=fbtnc_359)
btnc_359.grid(row=0,column=3)
btnc_360 = Button(frmc_72, bg=list_c[359], font=("", 36), command=fbtnc_360)
btnc_360.grid(row=0,column=4)

frmc_73 = Frame(big_frm3)
frmc_73.grid(row=4, column=2, padx=20)

btnc_361 = Button(frmc_73, bg=list_c[360], font=("", 36), command=fbtnc_361)
btnc_361.grid(row=0,column=0)
btnc_362 = Button(frmc_73, bg=list_c[361], font=("", 36), command=fbtnc_362)
btnc_362.grid(row=0,column=1)
btnc_363 = Button(frmc_73, bg=list_c[362], font=("", 36), command=fbtnc_363)
btnc_363.grid(row=0,column=2)
btnc_364 = Button(frmc_73, bg=list_c[363], font=("", 36), command=fbtnc_364)
btnc_364.grid(row=0,column=3)
btnc_365 = Button(frmc_73, bg=list_c[364], font=("", 36), command=fbtnc_365)
btnc_365.grid(row=0,column=4)

frmc_74 = Frame(big_frm3)
frmc_74.grid(row=4, column=3)

btnc_366 = Button(frmc_74, bg=list_c[365], font=("", 36), command=fbtnc_366)
btnc_366.grid(row=0,column=0)
btnc_367 = Button(frmc_74, bg=list_c[366], font=("", 36), command=fbtnc_367)
btnc_367.grid(row=0,column=1)
btnc_368 = Button(frmc_74, bg=list_c[367], font=("", 36), command=fbtnc_368)
btnc_368.grid(row=0,column=2)
btnc_369 = Button(frmc_74, bg=list_c[368], font=("", 36), command=fbtnc_369)
btnc_369.grid(row=0,column=3)
btnc_370 = Button(frmc_74, bg=list_c[369], font=("", 36), command=fbtnc_360)
btnc_370.grid(row=0,column=4)

frmc_75 = Frame(big_frm3)
frmc_75.grid(row=4, column=4, padx=20, pady=20)

btnc_371 = Button(frmc_75, bg=list_c[370], font=("", 36), command=fbtnc_371)
btnc_371.grid(row=0,column=0)
btnc_372 = Button(frmc_75, bg=list_c[371], font=("", 36), command=fbtnc_372)
btnc_372.grid(row=0,column=1)
btnc_373 = Button(frmc_75, bg=list_c[372], font=("", 36), command=fbtnc_373)
btnc_373.grid(row=0,column=2)
btnc_374 = Button(frmc_75, bg=list_c[373], font=("", 36), command=fbtnc_374)
btnc_374.grid(row=0,column=3)
btnc_375 = Button(frmc_75, bg=list_c[374], font=("", 36), command=fbtnc_375)
btnc_375.grid(row=0,column=4)



#-----------------------------------------------------------------------------------------------------------------------------------------



big_frm4 = Frame(root, bg="#f15bb5")

frmc_76 = Frame(big_frm4)
frmc_76.grid(row=0, column=0, padx=20)

btnc_376 = Button(frmc_76, bg=list_c[375], font=("", 36), command=fbtnc_376)
btnc_376.grid(row=0,column=0)
btnc_377 = Button(frmc_76, bg=list_c[376], font=("", 36), command=fbtnc_377)
btnc_377.grid(row=0,column=1)
btnc_378 = Button(frmc_76, bg=list_c[377], font=("", 36), command=fbtnc_378)
btnc_378.grid(row=0,column=2)
btnc_379 = Button(frmc_76, bg=list_c[378], font=("", 36), command=fbtnc_379)
btnc_379.grid(row=0,column=3)
btnc_380 = Button(frmc_76, bg=list_c[379], font=("", 36), command=fbtnc_380)
btnc_380.grid(row=0,column=4)

frmc_77 = Frame(big_frm4)
frmc_77.grid(row=0, column=1)

btnc_381 = Button(frmc_77, bg=list_c[380], font=("", 36), command=fbtnc_381)
btnc_381.grid(row=0,column=0)
btnc_382 = Button(frmc_77, bg=list_c[381], font=("", 36), command=fbtnc_382)
btnc_382.grid(row=0,column=1)
btnc_383 = Button(frmc_77, bg=list_c[382], font=("", 36), command=fbtnc_383)
btnc_383.grid(row=0,column=2)
btnc_384 = Button(frmc_77, bg=list_c[383], font=("", 36), command=fbtnc_384)
btnc_384.grid(row=0,column=3)
btnc_385 = Button(frmc_77, bg=list_c[384], font=("", 36), command=fbtnc_385)
btnc_385.grid(row=0,column=4)

frmc_78 = Frame(big_frm4)
frmc_78.grid(row=0, column=2, padx=20)

btnc_386 = Button(frmc_78, bg=list_c[385], font=("", 36), command=fbtnc_386)
btnc_386.grid(row=0,column=0)
btnc_387 = Button(frmc_78, bg=list_c[386], font=("", 36), command=fbtnc_387)
btnc_387.grid(row=0,column=1)
btnc_388 = Button(frmc_78, bg=list_c[387], font=("", 36), command=fbtnc_388)
btnc_388.grid(row=0,column=2)
btnc_389 = Button(frmc_78, bg=list_c[388], font=("", 36), command=fbtnc_389)
btnc_389.grid(row=0,column=3)
btnc_390 = Button(frmc_78, bg=list_c[389], font=("", 36), command=fbtnc_390)
btnc_390.grid(row=0,column=4)

frmc_79 = Frame(big_frm4)
frmc_79.grid(row=0, column=3)

btnc_391 = Button(frmc_79, bg=list_c[390], font=("", 36), command=fbtnc_391)
btnc_391.grid(row=0,column=0)
btnc_392 = Button(frmc_79, bg=list_c[391], font=("", 36), command=fbtnc_392)
btnc_392.grid(row=0,column=1)
btnc_393 = Button(frmc_79, bg=list_c[392], font=("", 36), command=fbtnc_393)
btnc_393.grid(row=0,column=2)
btnc_394 = Button(frmc_79, bg=list_c[393], font=("", 36), command=fbtnc_394)
btnc_394.grid(row=0,column=3)
btnc_395 = Button(frmc_79, bg=list_c[394], font=("", 36), command=fbtnc_395)
btnc_395.grid(row=0,column=4)

frmc_80 = Frame(big_frm4)
frmc_80.grid(row=0, column=4, padx=20, pady=20)

btnc_396 = Button(frmc_80, bg=list_c[395], font=("", 36), command=fbtnc_396)
btnc_396.grid(row=0,column=0)
btnc_397 = Button(frmc_80, bg=list_c[396], font=("", 36), command=fbtnc_397)
btnc_397.grid(row=0,column=1)
btnc_398 = Button(frmc_80, bg=list_c[397], font=("", 36), command=fbtnc_398)
btnc_398.grid(row=0,column=2)
btnc_399 = Button(frmc_80, bg=list_c[398], font=("", 36), command=fbtnc_399)
btnc_399.grid(row=0,column=3)
btnc_400 = Button(frmc_80, bg=list_c[399], font=("", 36), command=fbtnc_400)
btnc_400.grid(row=0,column=4)

frmc_81 = Frame(big_frm4)
frmc_81.grid(row=1, column=0, padx=20)

btnc_401 = Button(frmc_81, bg=list_c[400], font=("", 36), command=fbtnc_401)
btnc_401.grid(row=0,column=0)
btnc_402 = Button(frmc_81, bg=list_c[401], font=("", 36), command=fbtnc_402)
btnc_402.grid(row=0,column=1)
btnc_403 = Button(frmc_81, bg=list_c[402], font=("", 36), command=fbtnc_403)
btnc_403.grid(row=0,column=2)
btnc_404 = Button(frmc_81, bg=list_c[403], font=("", 36), command=fbtnc_404)
btnc_404.grid(row=0,column=3)
btnc_405 = Button(frmc_81, bg=list_c[404], font=("", 36), command=fbtnc_405)
btnc_405.grid(row=0,column=4)

frmc_82 = Frame(big_frm4)
frmc_82.grid(row=1, column=1)

btnc_406 = Button(frmc_82, bg=list_c[405], font=("", 36), command=fbtnc_406)
btnc_406.grid(row=0,column=0)
btnc_407 = Button(frmc_82, bg=list_c[406], font=("", 36), command=fbtnc_407)
btnc_407.grid(row=0,column=1)
btnc_408 = Button(frmc_82, bg=list_c[407], font=("", 36), command=fbtnc_408)
btnc_408.grid(row=0,column=2)
btnc_409 = Button(frmc_82, bg=list_c[408], font=("", 36), command=fbtnc_409)
btnc_409.grid(row=0,column=3)
btnc_410 = Button(frmc_82, bg=list_c[409], font=("", 36), command=fbtnc_410)
btnc_410.grid(row=0,column=4)

frmc_83 = Frame(big_frm4)
frmc_83.grid(row=1, column=2, padx=20)

btnc_411 = Button(frmc_83, bg=list_c[410], font=("", 36), command=fbtnc_411)
btnc_411.grid(row=0,column=0)
btnc_412 = Button(frmc_83, bg=list_c[411], font=("", 36), command=fbtnc_412)
btnc_412.grid(row=0,column=1)
btnc_413 = Button(frmc_83, bg=list_c[412], font=("", 36), command=fbtnc_413)
btnc_413.grid(row=0,column=2)
btnc_414 = Button(frmc_83, bg=list_c[413], font=("", 36), command=fbtnc_414)
btnc_414.grid(row=0,column=3)
btnc_415 = Button(frmc_83, bg=list_c[414], font=("", 36), command=fbtnc_415)
btnc_415.grid(row=0,column=4)

frmc_84 = Frame(big_frm4)
frmc_84.grid(row=1, column=3)

btnc_416 = Button(frmc_84, bg=list_c[415], font=("", 36), command=fbtnc_416)
btnc_416.grid(row=0,column=0)
btnc_417 = Button(frmc_84, bg=list_c[416], font=("", 36), command=fbtnc_417)
btnc_417.grid(row=0,column=1)
btnc_418 = Button(frmc_84, bg=list_c[417], font=("", 36), command=fbtnc_418)
btnc_418.grid(row=0,column=2)
btnc_419 = Button(frmc_84, bg=list_c[418], font=("", 36), command=fbtnc_419)
btnc_419.grid(row=0,column=3)
btnc_420 = Button(frmc_84, bg=list_c[419], font=("", 36), command=fbtnc_420)
btnc_420.grid(row=0,column=4)

frmc_85 = Frame(big_frm4)
frmc_85.grid(row=1, column=4, padx=20)

btnc_421 = Button(frmc_85, bg=list_c[420], font=("", 36), command=fbtnc_421)
btnc_421.grid(row=0,column=0)
btnc_422 = Button(frmc_85, bg=list_c[421], font=("", 36), command=fbtnc_422)
btnc_422.grid(row=0,column=1)
btnc_423 = Button(frmc_85, bg=list_c[422], font=("", 36), command=fbtnc_423)
btnc_423.grid(row=0,column=2)
btnc_424 = Button(frmc_85, bg=list_c[423], font=("", 36), command=fbtnc_424)
btnc_424.grid(row=0,column=3)
btnc_425 = Button(frmc_85, bg=list_c[424], font=("", 36), command=fbtnc_425)
btnc_425.grid(row=0,column=4)

frmc_86 = Frame(big_frm4)
frmc_86.grid(row=2, column=0, padx=20)

btnc_426 = Button(frmc_86, bg=list_c[425], font=("", 36), command=fbtnc_426)
btnc_426.grid(row=0,column=0)
btnc_427 = Button(frmc_86, bg=list_c[426], font=("", 36), command=fbtnc_427)
btnc_427.grid(row=0,column=1)
btnc_428 = Button(frmc_86, bg=list_c[427], font=("", 36), command=fbtnc_428)
btnc_428.grid(row=0,column=2)
btnc_429 = Button(frmc_86, bg=list_c[428], font=("", 36), command=fbtnc_429)
btnc_429.grid(row=0,column=3)
btnc_430 = Button(frmc_86, bg=list_c[429], font=("", 36), command=fbtnc_430)
btnc_430.grid(row=0,column=4)

frmc_87 = Frame(big_frm4)
frmc_87.grid(row=2, column=1)

btnc_431 = Button(frmc_87, bg=list_c[430], font=("", 36), command=fbtnc_431)
btnc_431.grid(row=0,column=0)
btnc_432 = Button(frmc_87, bg=list_c[431], font=("", 36), command=fbtnc_432)
btnc_432.grid(row=0,column=1)
btnc_433 = Button(frmc_87, bg=list_c[432], font=("", 36), command=fbtnc_433)
btnc_433.grid(row=0,column=2)
btnc_434 = Button(frmc_87, bg=list_c[433], font=("", 36), command=fbtnc_434)
btnc_434.grid(row=0,column=3)
btnc_435 = Button(frmc_87, bg=list_c[434], font=("", 36), command=fbtnc_435)
btnc_435.grid(row=0,column=4)

frmc_88 = Frame(big_frm4)
frmc_88.grid(row=2, column=2, padx=20)

btnc_436 = Button(frmc_88, bg=list_c[435], font=("", 36), command=fbtnc_436)
btnc_436.grid(row=0,column=0)
btnc_437 = Button(frmc_88, bg=list_c[436], font=("", 36), command=fbtnc_437)
btnc_437.grid(row=0,column=1)
btnc_438 = Button(frmc_88, bg=list_c[437], font=("", 36), command=fbtnc_438)
btnc_438.grid(row=0,column=2)
btnc_439 = Button(frmc_88, bg=list_c[438], font=("", 36), command=fbtnc_439)
btnc_439.grid(row=0,column=3)
btnc_440 = Button(frmc_88, bg=list_c[439], font=("", 36), command=fbtnc_440)
btnc_440.grid(row=0,column=4)

frmc_89 = Frame(big_frm4)
frmc_89.grid(row=2, column=3)

btnc_441 = Button(frmc_89, bg=list_c[440], font=("", 36), command=fbtnc_441)
btnc_441.grid(row=0,column=0)
btnc_442 = Button(frmc_89, bg=list_c[441], font=("", 36), command=fbtnc_442)
btnc_442.grid(row=0,column=1)
btnc_443 = Button(frmc_89, bg=list_c[442], font=("", 36), command=fbtnc_443)
btnc_443.grid(row=0,column=2)
btnc_444 = Button(frmc_89, bg=list_c[443], font=("", 36), command=fbtnc_444)
btnc_444.grid(row=0,column=3)
btnc_445 = Button(frmc_89, bg=list_c[444], font=("", 36), command=fbtnc_445)
btnc_445.grid(row=0,column=4)

frmc_90 = Frame(big_frm4)
frmc_90.grid(row=2, column=4, padx=20, pady=20)

btnc_446 = Button(frmc_90, bg=list_c[445], font=("", 36), command=fbtnc_446)
btnc_446.grid(row=0,column=0)
btnc_447 = Button(frmc_90, bg=list_c[446], font=("", 36), command=fbtnc_447)
btnc_447.grid(row=0,column=1)
btnc_448 = Button(frmc_90, bg=list_c[447], font=("", 36), command=fbtnc_448)
btnc_448.grid(row=0,column=2)
btnc_449 = Button(frmc_90, bg=list_c[448], font=("", 36), command=fbtnc_449)
btnc_449.grid(row=0,column=3)
btnc_450 = Button(frmc_90, bg=list_c[449], font=("", 36), command=fbtnc_450)
btnc_450.grid(row=0,column=4)

frmc_91 = Frame(big_frm4)
frmc_91.grid(row=3, column=0, padx=20)

btnc_451 = Button(frmc_91, bg=list_c[450], font=("", 36), command=fbtnc_451)
btnc_451.grid(row=0,column=0)
btnc_452 = Button(frmc_91, bg=list_c[451], font=("", 36), command=fbtnc_452)
btnc_452.grid(row=0,column=1)
btnc_453 = Button(frmc_91, bg=list_c[452], font=("", 36), command=fbtnc_453)
btnc_453.grid(row=0,column=2)
btnc_454 = Button(frmc_91, bg=list_c[453], font=("", 36), command=fbtnc_454)
btnc_454.grid(row=0,column=3)
btnc_455 = Button(frmc_91, bg=list_c[454], font=("", 36), command=fbtnc_455)
btnc_455.grid(row=0,column=4)

frmc_92 = Frame(big_frm4)
frmc_92.grid(row=3, column=1)

btnc_456 = Button(frmc_92, bg=list_c[455], font=("", 36), command=fbtnc_456)
btnc_456.grid(row=0,column=0)
btnc_457 = Button(frmc_92, bg=list_c[456], font=("", 36), command=fbtnc_457)
btnc_457.grid(row=0,column=1)
btnc_458 = Button(frmc_92, bg=list_c[457], font=("", 36), command=fbtnc_458)
btnc_458.grid(row=0,column=2)
btnc_459 = Button(frmc_92, bg=list_c[458], font=("", 36), command=fbtnc_459)
btnc_459.grid(row=0,column=3)
btnc_460 = Button(frmc_92, bg=list_c[459], font=("", 36), command=fbtnc_460)
btnc_460.grid(row=0,column=4)

frmc_93 = Frame(big_frm4)
frmc_93.grid(row=3, column=2, padx=20)

btnc_461 = Button(frmc_93, bg=list_c[460], font=("", 36), command=fbtnc_461)
btnc_461.grid(row=0,column=0)
btnc_462 = Button(frmc_93, bg=list_c[461], font=("", 36), command=fbtnc_462)
btnc_462.grid(row=0,column=1)
btnc_463 = Button(frmc_93, bg=list_c[462], font=("", 36), command=fbtnc_463)
btnc_463.grid(row=0,column=2)
btnc_464 = Button(frmc_93, bg=list_c[463], font=("", 36), command=fbtnc_464)
btnc_464.grid(row=0,column=3)
btnc_465 = Button(frmc_93, bg=list_c[464], font=("", 36), command=fbtnc_465)
btnc_465.grid(row=0,column=4)


frmc_94 = Frame(big_frm4)
frmc_94.grid(row=3, column=3)

btnc_466 = Button(frmc_94, bg=list_c[465], font=("", 36), command=fbtnc_466)
btnc_466.grid(row=0,column=0)
btnc_467 = Button(frmc_94, bg=list_c[466], font=("", 36), command=fbtnc_467)
btnc_467.grid(row=0,column=1)
btnc_468 = Button(frmc_94, bg=list_c[467], font=("", 36), command=fbtnc_468)
btnc_468.grid(row=0,column=2)
btnc_469 = Button(frmc_94, bg=list_c[468], font=("", 36), command=fbtnc_469)
btnc_469.grid(row=0,column=3)
btnc_470 = Button(frmc_94, bg=list_c[469], font=("", 36), command=fbtnc_470)
btnc_470.grid(row=0,column=4)

frmc_95 = Frame(big_frm4)
frmc_95.grid(row=3, column=4, padx=20)

btnc_471 = Button(frmc_95, bg=list_c[470], font=("", 36), command=fbtnc_471)
btnc_471.grid(row=0,column=0)
btnc_472 = Button(frmc_95, bg=list_c[471], font=("", 36), command=fbtnc_472)
btnc_472.grid(row=0,column=1)
btnc_473 = Button(frmc_95, bg=list_c[472], font=("", 36), command=fbtnc_473)
btnc_473.grid(row=0,column=2)
btnc_474 = Button(frmc_95, bg=list_c[473], font=("", 36), command=fbtnc_474)
btnc_474.grid(row=0,column=3)
btnc_475 = Button(frmc_95, bg=list_c[474], font=("", 36), command=fbtnc_475)
btnc_475.grid(row=0,column=4)


frmc_96 = Frame(big_frm4)
frmc_96.grid(row=4, column=0, padx=20)

btnc_476 = Button(frmc_96, bg=list_c[475], font=("", 36), command=fbtnc_476)
btnc_476.grid(row=0,column=0)
btnc_477 = Button(frmc_96, bg=list_c[476], font=("", 36), command=fbtnc_477)
btnc_477.grid(row=0,column=1)
btnc_478 = Button(frmc_96, bg=list_c[477], font=("", 36), command=fbtnc_478)
btnc_478.grid(row=0,column=2)
btnc_479 = Button(frmc_96, bg=list_c[478], font=("", 36), command=fbtnc_479)
btnc_479.grid(row=0,column=3)
btnc_480 = Button(frmc_96, bg=list_c[479], font=("", 36), command=fbtnc_480)
btnc_480.grid(row=0,column=4)

frmc_97 = Frame(big_frm4)
frmc_97.grid(row=4, column=1)

btnc_481 = Button(frmc_97, bg=list_c[480], font=("", 36), command=fbtnc_481)
btnc_481.grid(row=0,column=0)
btnc_482 = Button(frmc_97, bg=list_c[481], font=("", 36), command=fbtnc_482)
btnc_482.grid(row=0,column=1)
btnc_483 = Button(frmc_97, bg=list_c[482], font=("", 36), command=fbtnc_483)
btnc_483.grid(row=0,column=2)
btnc_484 = Button(frmc_97, bg=list_c[483], font=("", 36), command=fbtnc_484)
btnc_484.grid(row=0,column=3)
btnc_485 = Button(frmc_97, bg=list_c[484], font=("", 36), command=fbtnc_485)
btnc_485.grid(row=0,column=4)


frmc_98 = Frame(big_frm4)
frmc_98.grid(row=4, column=2, padx=20)

btnc_486 = Button(frmc_98, bg=list_c[485], font=("", 36), command=fbtnc_486)
btnc_486.grid(row=0,column=0)
btnc_487 = Button(frmc_98, bg=list_c[486], font=("", 36), command=fbtnc_487)
btnc_487.grid(row=0,column=1)
btnc_488 = Button(frmc_98, bg=list_c[487], font=("", 36), command=fbtnc_488)
btnc_488.grid(row=0,column=2)
btnc_489 = Button(frmc_98, bg=list_c[488], font=("", 36), command=fbtnc_489)
btnc_489.grid(row=0,column=3)
btnc_490 = Button(frmc_98, bg=list_c[489], font=("", 36), command=fbtnc_490)
btnc_490.grid(row=0,column=4)

frmc_99 = Frame(big_frm4)
frmc_99.grid(row=4, column=3)

btnc_491 = Button(frmc_99, bg=list_c[490], font=("", 36), command=fbtnc_491)
btnc_491.grid(row=0,column=0)
btnc_492 = Button(frmc_99, bg=list_c[491], font=("", 36), command=fbtnc_492)
btnc_492.grid(row=0,column=1)
btnc_493 = Button(frmc_99, bg=list_c[492], font=("", 36), command=fbtnc_493)
btnc_493.grid(row=0,column=2)
btnc_494 = Button(frmc_99, bg=list_c[493], font=("", 36), command=fbtnc_494)
btnc_494.grid(row=0,column=3)
btnc_495 = Button(frmc_99, bg=list_c[494], font=("", 36), command=fbtnc_495)
btnc_495.grid(row=0,column=4)

frmc_100 = Frame(big_frm4)
frmc_100.grid(row=4, column=4, padx=20, pady=20)

btnc_496 = Button(frmc_100, bg=list_c[495], font=("", 36), command=fbtnc_496)
btnc_496.grid(row=0,column=0)
btnc_497 = Button(frmc_100, bg=list_c[496], font=("", 36), command=fbtnc_497)
btnc_497.grid(row=0,column=1)
btnc_498 = Button(frmc_100, bg=list_c[497], font=("", 36), command=fbtnc_498)
btnc_498.grid(row=0,column=2)
btnc_499 = Button(frmc_100, bg=list_c[498], font=("", 36), command=fbtnc_499)
btnc_499.grid(row=0,column=3)
btnc_500 = Button(frmc_100, bg=list_c[499], font=("", 36), command=fbtnc_500)
btnc_500.grid(row=0,column=4)



#----------------------------------------------------------------------------------------------------------------------------------------------------



big_frm5 = Frame(root, bg="#f15bb5")

frmc_101 = Frame(big_frm5)
frmc_101.grid(row=0, column=0, padx=20)

btnc_501 = Button(frmc_101, bg=list_c[500], font=("", 36), command=fbtnc_501)
btnc_501.grid(row=0,column=0)
btnc_502 = Button(frmc_101, bg=list_c[501], font=("", 36), command=fbtnc_502)
btnc_502.grid(row=0,column=1)
btnc_503 = Button(frmc_101, bg=list_c[502], font=("", 36), command=fbtnc_503)
btnc_503.grid(row=0,column=2)
btnc_504 = Button(frmc_101, bg=list_c[503], font=("", 36), command=fbtnc_504)
btnc_504.grid(row=0,column=3)
btnc_505 = Button(frmc_101, bg=list_c[504], font=("", 36), command=fbtnc_505)
btnc_505.grid(row=0,column=4)

frmc_102 = Frame(big_frm5)
frmc_102.grid(row=0, column=1)

btnc_506 = Button(frmc_102, bg=list_c[505], font=("", 36), command=fbtnc_506)
btnc_506.grid(row=0,column=0)
btnc_507 = Button(frmc_102, bg=list_c[506], font=("", 36), command=fbtnc_507)
btnc_507.grid(row=0,column=1)
btnc_508 = Button(frmc_102, bg=list_c[507], font=("", 36), command=fbtnc_508)
btnc_508.grid(row=0,column=2)
btnc_509 = Button(frmc_102, bg=list_c[508], font=("", 36), command=fbtnc_509)
btnc_509.grid(row=0,column=3)
btnc_510 = Button(frmc_102, bg=list_c[509], font=("", 36), command=fbtnc_510)
btnc_510.grid(row=0,column=4)

frmc_103 = Frame(big_frm5)
frmc_103.grid(row=0, column=2, padx=20)

btnc_511 = Button(frmc_103, bg=list_c[510], font=("", 36), command=fbtnc_511)
btnc_511.grid(row=0,column=0)
btnc_512 = Button(frmc_103, bg=list_c[511], font=("", 36), command=fbtnc_512)
btnc_512.grid(row=0,column=1)
btnc_513 = Button(frmc_103, bg=list_c[512], font=("", 36), command=fbtnc_513)
btnc_513.grid(row=0,column=2)
btnc_514 = Button(frmc_103, bg=list_c[513], font=("", 36), command=fbtnc_514)
btnc_514.grid(row=0,column=3)
btnc_515 = Button(frmc_103, bg=list_c[514], font=("", 36), command=fbtnc_515)
btnc_515.grid(row=0,column=4)

frmc_104 = Frame(big_frm5)
frmc_104.grid(row=0, column=3)

btnc_516 = Button(frmc_104, bg=list_c[515], font=("", 36), command=fbtnc_516)
btnc_516.grid(row=0,column=0)
btnc_517 = Button(frmc_104, bg=list_c[516], font=("", 36), command=fbtnc_517)
btnc_517.grid(row=0,column=1)
btnc_518 = Button(frmc_104, bg=list_c[517], font=("", 36), command=fbtnc_518)
btnc_518.grid(row=0,column=2)
btnc_519 = Button(frmc_104, bg=list_c[518], font=("", 36), command=fbtnc_519)
btnc_519.grid(row=0,column=3)
btnc_520 = Button(frmc_104, bg=list_c[519], font=("", 36), command=fbtnc_520)
btnc_520.grid(row=0,column=4)

frmc_105 = Frame(big_frm5)
frmc_105.grid(row=0, column=4, padx=20, pady=20)

btnc_521 = Button(frmc_105, bg=list_c[520], font=("", 36), command=fbtnc_521)
btnc_521.grid(row=0,column=0)
btnc_522 = Button(frmc_105, bg=list_c[521], font=("", 36), command=fbtnc_522)
btnc_522.grid(row=0,column=1)
btnc_523 = Button(frmc_105, bg=list_c[522], font=("", 36), command=fbtnc_523)
btnc_523.grid(row=0,column=2)
btnc_524 = Button(frmc_105, bg=list_c[523], font=("", 36), command=fbtnc_524)
btnc_524.grid(row=0,column=3)
btnc_525 = Button(frmc_105, bg=list_c[524], font=("", 36), command=fbtnc_525)
btnc_525.grid(row=0,column=4)

frmc_106 = Frame(big_frm5)
frmc_106.grid(row=1, column=0, padx=20)

btnc_526 = Button(frmc_106, bg=list_c[525], font=("", 36), command=fbtnc_526)
btnc_526.grid(row=0,column=0)
btnc_527 = Button(frmc_106, bg=list_c[526], font=("", 36), command=fbtnc_527)
btnc_527.grid(row=0,column=1)
btnc_528 = Button(frmc_106, bg=list_c[527], font=("", 36), command=fbtnc_528)
btnc_528.grid(row=0,column=2)
btnc_529 = Button(frmc_106, bg=list_c[528], font=("", 36), command=fbtnc_529)
btnc_529.grid(row=0,column=3)
btnc_530 = Button(frmc_106, bg=list_c[529], font=("", 36), command=fbtnc_530)
btnc_530.grid(row=0,column=4)

frmc_107= Frame(big_frm5)
frmc_107.grid(row=1, column=1)

btnc_531 = Button(frmc_107, bg=list_c[530], font=("", 36), command=fbtnc_531)
btnc_531.grid(row=0,column=0)
btnc_532 = Button(frmc_107, bg=list_c[531], font=("", 36), command=fbtnc_532)
btnc_532.grid(row=0,column=1)
btnc_533 = Button(frmc_107, bg=list_c[532], font=("", 36), command=fbtnc_533)
btnc_533.grid(row=0,column=2)
btnc_534 = Button(frmc_107, bg=list_c[533], font=("", 36), command=fbtnc_534)
btnc_534.grid(row=0,column=3)
btnc_535 = Button(frmc_107, bg=list_c[534], font=("", 36), command=fbtnc_535)
btnc_535.grid(row=0,column=4)

frmc_108 = Frame(big_frm5)
frmc_108.grid(row=1, column=2, padx=20)

btnc_536 = Button(frmc_108, bg=list_c[535], font=("", 36), command=fbtnc_536)
btnc_536.grid(row=0,column=0)
btnc_537 = Button(frmc_108, bg=list_c[536], font=("", 36), command=fbtnc_537)
btnc_537.grid(row=0,column=1)
btnc_538 = Button(frmc_108, bg=list_c[537], font=("", 36), command=fbtnc_538)
btnc_538.grid(row=0,column=2)
btnc_539 = Button(frmc_108, bg=list_c[538], font=("", 36), command=fbtnc_539)
btnc_539.grid(row=0,column=3)
btnc_540 = Button(frmc_108, bg=list_c[539], font=("", 36), command=fbtnc_540)
btnc_540.grid(row=0,column=4)

frmc_109 = Frame(big_frm5)
frmc_109.grid(row=1, column=3)

btnc_541 = Button(frmc_109, bg=list_c[500], font=("", 36), command=fbtnc_501)
btnc_541.grid(row=0,column=0)
btnc_542 = Button(frmc_109, bg=list_c[501], font=("", 36), command=fbtnc_502)
btnc_542.grid(row=0,column=1)
btnc_543 = Button(frmc_109, bg=list_c[502], font=("", 36), command=fbtnc_503)
btnc_543.grid(row=0,column=2)
btnc_544 = Button(frmc_109, bg=list_c[503], font=("", 36), command=fbtnc_504)
btnc_544.grid(row=0,column=3)
btnc_545 = Button(frmc_109, bg=list_c[504], font=("", 36), command=fbtnc_505)
btnc_545.grid(row=0,column=4)

frmc_110 = Frame(big_frm5)
frmc_110.grid(row=1, column=4, padx=20)

btnc_546 = Button(frmc_110, bg=list_c[545], font=("", 36), command=fbtnc_546)
btnc_546.grid(row=0,column=0)
btnc_547 = Button(frmc_110, bg=list_c[546], font=("", 36), command=fbtnc_547)
btnc_547.grid(row=0,column=1)
btnc_548 = Button(frmc_110, bg=list_c[547], font=("", 36), command=fbtnc_548)
btnc_548.grid(row=0,column=2)
btnc_549 = Button(frmc_110, bg=list_c[548], font=("", 36), command=fbtnc_549)
btnc_549.grid(row=0,column=3)
btnc_550 = Button(frmc_110, bg=list_c[549], font=("", 36), command=fbtnc_550)
btnc_550.grid(row=0,column=4)

frmc_111= Frame(big_frm5)
frmc_111.grid(row=2, column=0, padx=20)

btnc_551 = Button(frmc_111, bg=list_c[550], font=("", 36), command=fbtnc_551)
btnc_551.grid(row=0,column=0)
btnc_552 = Button(frmc_111, bg=list_c[551], font=("", 36), command=fbtnc_552)
btnc_552.grid(row=0,column=1)
btnc_553 = Button(frmc_111, bg=list_c[552], font=("", 36), command=fbtnc_553)
btnc_553.grid(row=0,column=2)
btnc_554 = Button(frmc_111, bg=list_c[553], font=("", 36), command=fbtnc_554)
btnc_554.grid(row=0,column=3)
btnc_555 = Button(frmc_111, bg=list_c[554], font=("", 36), command=fbtnc_555)
btnc_555.grid(row=0,column=4)

frmc_112 = Frame(big_frm5)
frmc_112.grid(row=2, column=1)

btnc_556 = Button(frmc_112, bg=list_c[555], font=("", 36), command=fbtnc_556)
btnc_556.grid(row=0,column=0)
btnc_557 = Button(frmc_112, bg=list_c[556], font=("", 36), command=fbtnc_557)
btnc_557.grid(row=0,column=1)
btnc_558 = Button(frmc_112, bg=list_c[557], font=("", 36), command=fbtnc_558)
btnc_558.grid(row=0,column=2)
btnc_559 = Button(frmc_112, bg=list_c[558], font=("", 36), command=fbtnc_559)
btnc_559.grid(row=0,column=3)
btnc_560 = Button(frmc_112, bg=list_c[559], font=("", 36), command=fbtnc_560)
btnc_560.grid(row=0,column=4)

frmc_113 = Frame(big_frm5)
frmc_113.grid(row=2, column=2, padx=20)

btnc_561 = Button(frmc_113, bg=list_c[560], font=("", 36), command=fbtnc_561)
btnc_561.grid(row=0,column=0)
btnc_562 = Button(frmc_113, bg=list_c[561], font=("", 36), command=fbtnc_562)
btnc_562.grid(row=0,column=1)
btnc_563 = Button(frmc_113, bg=list_c[562], font=("", 36), command=fbtnc_563)
btnc_563.grid(row=0,column=2)
btnc_564 = Button(frmc_113, bg=list_c[563], font=("", 36), command=fbtnc_564)
btnc_564.grid(row=0,column=3)
btnc_565 = Button(frmc_113, bg=list_c[564], font=("", 36), command=fbtnc_565)
btnc_565.grid(row=0,column=4)

frmc_114 = Frame(big_frm5)
frmc_114.grid(row=2, column=3)

btnc_566 = Button(frmc_114, bg=list_c[565], font=("", 36), command=fbtnc_566)
btnc_566.grid(row=0,column=0)
btnc_567 = Button(frmc_114, bg=list_c[566], font=("", 36), command=fbtnc_567)
btnc_567.grid(row=0,column=1)
btnc_568 = Button(frmc_114, bg=list_c[567], font=("", 36), command=fbtnc_568)
btnc_568.grid(row=0,column=2)
btnc_569 = Button(frmc_114, bg=list_c[568], font=("", 36), command=fbtnc_569)
btnc_569.grid(row=0,column=3)
btnc_570 = Button(frmc_114, bg=list_c[569], font=("", 36), command=fbtnc_570)
btnc_570.grid(row=0,column=4)

frmc_115 = Frame(big_frm5)
frmc_115.grid(row=2, column=4, padx=20, pady=20)

btnc_571 = Button(frmc_115, bg=list_c[570], font=("", 36), command=fbtnc_571)
btnc_571.grid(row=0,column=0)
btnc_572 = Button(frmc_115, bg=list_c[571], font=("", 36), command=fbtnc_572)
btnc_572.grid(row=0,column=1)
btnc_573 = Button(frmc_115, bg=list_c[572], font=("", 36), command=fbtnc_573)
btnc_573.grid(row=0,column=2)
btnc_574 = Button(frmc_115, bg=list_c[573], font=("", 36), command=fbtnc_574)
btnc_574.grid(row=0,column=3)
btnc_575 = Button(frmc_115, bg=list_c[574], font=("", 36), command=fbtnc_575)
btnc_575.grid(row=0,column=4)

frmc_116 = Frame(big_frm5)
frmc_116.grid(row=3, column=0, padx=20)

btnc_576 = Button(frmc_116, bg=list_c[575], font=("", 36), command=fbtnc_576)
btnc_576.grid(row=0,column=0)
btnc_577 = Button(frmc_116, bg=list_c[576], font=("", 36), command=fbtnc_577)
btnc_577.grid(row=0,column=1)
btnc_578 = Button(frmc_116, bg=list_c[577], font=("", 36), command=fbtnc_578)
btnc_578.grid(row=0,column=2)
btnc_579 = Button(frmc_116, bg=list_c[578], font=("", 36), command=fbtnc_579)
btnc_579.grid(row=0,column=3)
btnc_580 = Button(frmc_116, bg=list_c[579], font=("", 36), command=fbtnc_580)
btnc_580.grid(row=0,column=4)

frmc_117 = Frame(big_frm5)
frmc_117.grid(row=3, column=1)

btnc_581 = Button(frmc_117, bg=list_c[580], font=("", 36), command=fbtnc_581)
btnc_581.grid(row=0,column=0)
btnc_582 = Button(frmc_117, bg=list_c[581], font=("", 36), command=fbtnc_582)
btnc_582.grid(row=0,column=1)
btnc_583 = Button(frmc_117, bg=list_c[582], font=("", 36), command=fbtnc_583)
btnc_583.grid(row=0,column=2)
btnc_584 = Button(frmc_117, bg=list_c[583], font=("", 36), command=fbtnc_584)
btnc_584.grid(row=0,column=3)
btnc_585 = Button(frmc_117, bg=list_c[584], font=("", 36), command=fbtnc_585)
btnc_585.grid(row=0,column=4)

frmc_118 = Frame(big_frm5)
frmc_118.grid(row=3, column=2, padx=20)

btnc_586 = Button(frmc_118, bg=list_c[585], font=("", 36), command=fbtnc_586)
btnc_586.grid(row=0,column=0)
btnc_587 = Button(frmc_118, bg=list_c[586], font=("", 36), command=fbtnc_587)
btnc_587.grid(row=0,column=1)
btnc_588 = Button(frmc_118, bg=list_c[587], font=("", 36), command=fbtnc_588)
btnc_588.grid(row=0,column=2)
btnc_589 = Button(frmc_118, bg=list_c[588], font=("", 36), command=fbtnc_589)
btnc_589.grid(row=0,column=3)
btnc_590 = Button(frmc_118, bg=list_c[589], font=("", 36), command=fbtnc_590)
btnc_590.grid(row=0,column=4)

frmc_119 = Frame(big_frm5)
frmc_119.grid(row=3, column=3)

btnc_591 = Button(frmc_119, bg=list_c[590], font=("", 36), command=fbtnc_591)
btnc_591.grid(row=0,column=0)
btnc_592 = Button(frmc_119, bg=list_c[591], font=("", 36), command=fbtnc_592)
btnc_592.grid(row=0,column=1)
btnc_593 = Button(frmc_119, bg=list_c[592], font=("", 36), command=fbtnc_593)
btnc_593.grid(row=0,column=2)
btnc_594 = Button(frmc_119, bg=list_c[593], font=("", 36), command=fbtnc_594)
btnc_594.grid(row=0,column=3)
btnc_595 = Button(frmc_119, bg=list_c[594], font=("", 36), command=fbtnc_595)
btnc_595.grid(row=0,column=4)

frmc_120 = Frame(big_frm5)
frmc_120.grid(row=3, column=4, padx=20)

btnc_596 = Button(frmc_120, bg=list_c[595], font=("", 36), command=fbtnc_596)
btnc_596.grid(row=0,column=0)
btnc_597 = Button(frmc_120, bg=list_c[596], font=("", 36), command=fbtnc_597)
btnc_597.grid(row=0,column=1)
btnc_598 = Button(frmc_120, bg=list_c[597], font=("", 36), command=fbtnc_598)
btnc_598.grid(row=0,column=2)
btnc_599 = Button(frmc_120, bg=list_c[598], font=("", 36), command=fbtnc_599)
btnc_599.grid(row=0,column=3)
btnc_600 = Button(frmc_120, bg=list_c[599], font=("", 36), command=fbtnc_600)
btnc_600.grid(row=0,column=4)

frmc_121 = Frame(big_frm5)
frmc_121.grid(row=4, column=0, padx=20)

btnc_601 = Button(frmc_121, bg=list_c[600], font=("", 36), command=fbtnc_601)
btnc_601.grid(row=0,column=0)
btnc_602 = Button(frmc_121, bg=list_c[601], font=("", 36), command=fbtnc_602)
btnc_602.grid(row=0,column=1)
btnc_603 = Button(frmc_121, bg=list_c[602], font=("", 36), command=fbtnc_603)
btnc_603.grid(row=0,column=2)
btnc_604 = Button(frmc_121, bg=list_c[603], font=("", 36), command=fbtnc_604)
btnc_604.grid(row=0,column=3)
btnc_605 = Button(frmc_121, bg=list_c[604], font=("", 36), command=fbtnc_605)
btnc_605.grid(row=0,column=4)

frmc_122 = Frame(big_frm5)
frmc_122.grid(row=4, column=1)

btnc_606 = Button(frmc_122, bg=list_c[605], font=("", 36), command=fbtnc_606)
btnc_606.grid(row=0,column=0)
btnc_607 = Button(frmc_122, bg=list_c[606], font=("", 36), command=fbtnc_607)
btnc_607.grid(row=0,column=1)
btnc_608 = Button(frmc_122, bg=list_c[607], font=("", 36), command=fbtnc_608)
btnc_608.grid(row=0,column=2)
btnc_609 = Button(frmc_122, bg=list_c[608], font=("", 36), command=fbtnc_609)
btnc_609.grid(row=0,column=3)
btnc_610 = Button(frmc_122, bg=list_c[609], font=("", 36), command=fbtnc_610)
btnc_610.grid(row=0,column=4)

frmc_123 = Frame(big_frm5)
frmc_123.grid(row=4, column=2, padx=20)

btnc_611 = Button(frmc_123, bg=list_c[610], font=("", 36), command=fbtnc_611)
btnc_611.grid(row=0,column=0)
btnc_612 = Button(frmc_123, bg=list_c[611], font=("", 36), command=fbtnc_612)
btnc_612.grid(row=0,column=1)
btnc_613 = Button(frmc_123, bg=list_c[612], font=("", 36), command=fbtnc_613)
btnc_613.grid(row=0,column=2)
btnc_614 = Button(frmc_123, bg=list_c[613], font=("", 36), command=fbtnc_614)
btnc_614.grid(row=0,column=3)
btnc_615 = Button(frmc_123, bg=list_c[614], font=("", 36), command=fbtnc_615)
btnc_615.grid(row=0,column=4)

frmc_124 = Frame(big_frm5)
frmc_124.grid(row=4, column=3)

btnc_616 = Button(frmc_124, bg=list_c[615], font=("", 36), command=fbtnc_616)
btnc_616.grid(row=0,column=0)
btnc_617 = Button(frmc_124, bg=list_c[616], font=("", 36), command=fbtnc_617)
btnc_617.grid(row=0,column=1)
btnc_618 = Button(frmc_124, bg=list_c[617], font=("", 36), command=fbtnc_618)
btnc_618.grid(row=0,column=2)
btnc_619 = Button(frmc_124, bg=list_c[618], font=("", 36), command=fbtnc_619)
btnc_619.grid(row=0,column=3)
btnc_620 = Button(frmc_124, bg=list_c[619], font=("", 36), command=fbtnc_620)
btnc_620.grid(row=0,column=4)

frmc_125 = Frame(big_frm5)
frmc_125.grid(row=4, column=4, padx=20, pady=20)

btnc_621 = Button(frmc_125, bg=list_c[620], font=("", 36), command=fbtnc_621)
btnc_621.grid(row=0,column=0)
btnc_622 = Button(frmc_125, bg=list_c[621], font=("", 36), command=fbtnc_622)
btnc_622.grid(row=0,column=1)
btnc_623 = Button(frmc_125, bg=list_c[622], font=("", 36), command=fbtnc_623)
btnc_623.grid(row=0,column=2)
btnc_624 = Button(frmc_125, bg=list_c[623], font=("", 36), command=fbtnc_624)
btnc_624.grid(row=0,column=3)
btnc_625 = Button(frmc_125, bg=list_c[624], font=("", 36), command=fbtnc_625)
btnc_625.grid(row=0,column=4)



#---------------------------------------------------------------------------------------------------------------------------------------

big_frm6 = Frame(root, bg="#f15bb5")

frmc_126 = Frame(big_frm6)
frmc_126.grid(row=0, column=0, padx=20)

btnc_626 = Button(frmc_126, bg=list_c[625], font=("", 36), command=fbtnc_626)
btnc_626.grid(row=0,column=0)
btnc_627 = Button(frmc_126, bg=list_c[626], font=("", 36), command=fbtnc_627)
btnc_627.grid(row=0,column=1)
btnc_628 = Button(frmc_126, bg=list_c[627], font=("", 36), command=fbtnc_628)
btnc_628.grid(row=0,column=2)
btnc_629 = Button(frmc_126, bg=list_c[628], font=("", 36), command=fbtnc_629)
btnc_629.grid(row=0,column=3)
btnc_630 = Button(frmc_126, bg=list_c[629], font=("", 36), command=fbtnc_630)
btnc_630.grid(row=0,column=4)

frmc_127 = Frame(big_frm6)
frmc_127.grid(row=0, column=1)

btnc_631 = Button(frmc_127, bg=list_c[630], font=("", 36), command=fbtnc_631)
btnc_631.grid(row=0,column=0)
btnc_632 = Button(frmc_127, bg=list_c[631], font=("", 36), command=fbtnc_632)
btnc_632.grid(row=0,column=1)
btnc_633 = Button(frmc_127, bg=list_c[632], font=("", 36), command=fbtnc_633)
btnc_633.grid(row=0,column=2)
btnc_634 = Button(frmc_127, bg=list_c[633], font=("", 36), command=fbtnc_634)
btnc_634.grid(row=0,column=3)
btnc_635 = Button(frmc_127, bg=list_c[634], font=("", 36), command=fbtnc_635)
btnc_635.grid(row=0,column=4)

frmc_128 = Frame(big_frm6)
frmc_128.grid(row=0, column=2, padx=20)

btnc_636 = Button(frmc_128, bg=list_c[635], font=("", 36), command=fbtnc_636)
btnc_636.grid(row=0,column=0)
btnc_637 = Button(frmc_128, bg=list_c[636], font=("", 36), command=fbtnc_637)
btnc_637.grid(row=0,column=1)
btnc_638 = Button(frmc_128, bg=list_c[637], font=("", 36), command=fbtnc_638)
btnc_638.grid(row=0,column=2)
btnc_639 = Button(frmc_128, bg=list_c[638], font=("", 36), command=fbtnc_639)
btnc_639.grid(row=0,column=3)
btnc_640 = Button(frmc_128, bg=list_c[639], font=("", 36), command=fbtnc_640)
btnc_640.grid(row=0,column=4)

frmc_129 = Frame(big_frm6)
frmc_129.grid(row=0, column=3)

btnc_641 = Button(frmc_129, bg=list_c[640], font=("", 36), command=fbtnc_641)
btnc_641.grid(row=0,column=0)
btnc_642 = Button(frmc_129, bg=list_c[641], font=("", 36), command=fbtnc_642)
btnc_642.grid(row=0,column=1)
btnc_643 = Button(frmc_129, bg=list_c[642], font=("", 36), command=fbtnc_643)
btnc_643.grid(row=0,column=2)
btnc_644 = Button(frmc_129, bg=list_c[643], font=("", 36), command=fbtnc_644)
btnc_644.grid(row=0,column=3)
btnc_645 = Button(frmc_129, bg=list_c[644], font=("", 36), command=fbtnc_645)
btnc_645.grid(row=0,column=4)

frmc_130 = Frame(big_frm6)
frmc_130.grid(row=0, column=4, padx=20, pady=20)

btnc_646 = Button(frmc_130, bg=list_c[645], font=("", 36), command=fbtnc_646)
btnc_646.grid(row=0,column=0)
btnc_647 = Button(frmc_130, bg=list_c[646], font=("", 36), command=fbtnc_647)
btnc_647.grid(row=0,column=1)
btnc_648 = Button(frmc_130, bg=list_c[647], font=("", 36), command=fbtnc_648)
btnc_648.grid(row=0,column=2)
btnc_649 = Button(frmc_130, bg=list_c[648], font=("", 36), command=fbtnc_649)
btnc_649.grid(row=0,column=3)
btnc_650 = Button(frmc_130, bg=list_c[649], font=("", 36), command=fbtnc_650)
btnc_650.grid(row=0,column=4)

frmc_131 = Frame(big_frm6)
frmc_131.grid(row=1, column=0, padx=20)

btnc_651 = Button(frmc_131, bg=list_c[650], font=("", 36), command=fbtnc_651)
btnc_651.grid(row=0,column=0)
btnc_652 = Button(frmc_131, bg=list_c[651], font=("", 36), command=fbtnc_652)
btnc_652.grid(row=0,column=1)
btnc_653 = Button(frmc_131, bg=list_c[652], font=("", 36), command=fbtnc_653)
btnc_653.grid(row=0,column=2)
btnc_654 = Button(frmc_131, bg=list_c[653], font=("", 36), command=fbtnc_654)
btnc_654.grid(row=0,column=3)
btnc_655 = Button(frmc_131, bg=list_c[654], font=("", 36), command=fbtnc_655)
btnc_655.grid(row=0,column=4)

frmc_132 = Frame(big_frm6)
frmc_132.grid(row=1, column=1)

btnc_656 = Button(frmc_132, bg=list_c[655], font=("", 36), command=fbtnc_656)
btnc_656.grid(row=0,column=0)
btnc_657 = Button(frmc_132, bg=list_c[656], font=("", 36), command=fbtnc_657)
btnc_657.grid(row=0,column=1)
btnc_658 = Button(frmc_132, bg=list_c[657], font=("", 36), command=fbtnc_658)
btnc_658.grid(row=0,column=2)
btnc_659 = Button(frmc_132, bg=list_c[658], font=("", 36), command=fbtnc_659)
btnc_659.grid(row=0,column=3)
btnc_660 = Button(frmc_132, bg=list_c[659], font=("", 36), command=fbtnc_660)
btnc_660.grid(row=0,column=4)

frmc_133 = Frame(big_frm6)
frmc_133.grid(row=1, column=2, padx=20)

btnc_661 = Button(frmc_133, bg=list_c[660], font=("", 36), command=fbtnc_661)
btnc_661.grid(row=0,column=0)
btnc_662 = Button(frmc_133, bg=list_c[661], font=("", 36), command=fbtnc_662)
btnc_662.grid(row=0,column=1)
btnc_663 = Button(frmc_133, bg=list_c[662], font=("", 36), command=fbtnc_663)
btnc_663.grid(row=0,column=2)
btnc_664 = Button(frmc_133, bg=list_c[663], font=("", 36), command=fbtnc_664)
btnc_664.grid(row=0,column=3)
btnc_665 = Button(frmc_133, bg=list_c[664], font=("", 36), command=fbtnc_665)
btnc_665.grid(row=0,column=4)

frmc_134 = Frame(big_frm6)
frmc_134.grid(row=1, column=3)

btnc_666 = Button(frmc_134, bg=list_c[665], font=("", 36), command=fbtnc_666)
btnc_666.grid(row=0,column=0)
btnc_667 = Button(frmc_134, bg=list_c[666], font=("", 36), command=fbtnc_667)
btnc_667.grid(row=0,column=1)
btnc_668 = Button(frmc_134, bg=list_c[667], font=("", 36), command=fbtnc_668)
btnc_668.grid(row=0,column=2)
btnc_669 = Button(frmc_134, bg=list_c[668], font=("", 36), command=fbtnc_669)
btnc_669.grid(row=0,column=3)
btnc_670 = Button(frmc_134, bg=list_c[669], font=("", 36), command=fbtnc_670)
btnc_670.grid(row=0,column=4)

frmc_135 = Frame(big_frm6)
frmc_135.grid(row=1, column=4, padx=20)

btnc_671 = Button(frmc_135, bg=list_c[670], font=("", 36), command=fbtnc_671)
btnc_671.grid(row=0,column=0)
btnc_672 = Button(frmc_135, bg=list_c[671], font=("", 36), command=fbtnc_672)
btnc_672.grid(row=0,column=1)
btnc_673 = Button(frmc_135, bg=list_c[672], font=("", 36), command=fbtnc_673)
btnc_673.grid(row=0,column=2)
btnc_674 = Button(frmc_135, bg=list_c[673], font=("", 36), command=fbtnc_674)
btnc_674.grid(row=0,column=3)
btnc_675 = Button(frmc_135, bg=list_c[674], font=("", 36), command=fbtnc_675)
btnc_675.grid(row=0,column=4)

frmc_136 = Frame(big_frm6)
frmc_136.grid(row=2, column=0, padx=20)

btnc_676 = Button(frmc_136, bg=list_c[675], font=("", 36), command=fbtnc_676)
btnc_676.grid(row=0,column=0)
btnc_677 = Button(frmc_136, bg=list_c[676], font=("", 36), command=fbtnc_677)
btnc_677.grid(row=0,column=1)
btnc_678 = Button(frmc_136, bg=list_c[677], font=("", 36), command=fbtnc_678)
btnc_678.grid(row=0,column=2)
btnc_679 = Button(frmc_136, bg=list_c[678], font=("", 36), command=fbtnc_679)
btnc_679.grid(row=0,column=3)
btnc_680 = Button(frmc_136, bg=list_c[679], font=("", 36), command=fbtnc_680)
btnc_680.grid(row=0,column=4)

frmc_137 = Frame(big_frm6)
frmc_137.grid(row=2, column=1)

btnc_681 = Button(frmc_137, bg=list_c[680], font=("", 36), command=fbtnc_681)
btnc_681.grid(row=0,column=0)
btnc_682 = Button(frmc_137, bg=list_c[681], font=("", 36), command=fbtnc_682)
btnc_682.grid(row=0,column=1)
btnc_683 = Button(frmc_137, bg=list_c[682], font=("", 36), command=fbtnc_683)
btnc_683.grid(row=0,column=2)
btnc_684 = Button(frmc_137, bg=list_c[683], font=("", 36), command=fbtnc_684)
btnc_684.grid(row=0,column=3)
btnc_685 = Button(frmc_137, bg=list_c[684], font=("", 36), command=fbtnc_685)
btnc_685.grid(row=0,column=4)

frmc_138 = Frame(big_frm6)
frmc_138.grid(row=2, column=2, padx=20)

btnc_686 = Button(frmc_138, bg=list_c[685], font=("", 36), command=fbtnc_686)
btnc_686.grid(row=0,column=0)
btnc_687 = Button(frmc_138, bg=list_c[686], font=("", 36), command=fbtnc_687)
btnc_687.grid(row=0,column=1)
btnc_688 = Button(frmc_138, bg=list_c[687], font=("", 36), command=fbtnc_688)
btnc_688.grid(row=0,column=2)
btnc_689 = Button(frmc_138, bg=list_c[688], font=("", 36), command=fbtnc_689)
btnc_689.grid(row=0,column=3)
btnc_690 = Button(frmc_138, bg=list_c[689], font=("", 36), command=fbtnc_690)
btnc_690.grid(row=0,column=4)

frmc_139 = Frame(big_frm6)
frmc_139.grid(row=2, column=3)

btnc_691 = Button(frmc_139, bg=list_c[690], font=("", 36), command=fbtnc_691)
btnc_691.grid(row=0,column=0)
btnc_692 = Button(frmc_139, bg=list_c[691], font=("", 36), command=fbtnc_692)
btnc_692.grid(row=0,column=1)
btnc_693 = Button(frmc_139, bg=list_c[692], font=("", 36), command=fbtnc_693)
btnc_693.grid(row=0,column=2)
btnc_694 = Button(frmc_139, bg=list_c[693], font=("", 36), command=fbtnc_694)
btnc_694.grid(row=0,column=3)
btnc_695 = Button(frmc_139, bg=list_c[694], font=("", 36), command=fbtnc_695)
btnc_695.grid(row=0,column=4)

frmc_140 = Frame(big_frm6)
frmc_140.grid(row=2, column=4, padx=20, pady=20)

btnc_696 = Button(frmc_140, bg=list_c[695], font=("", 36), command=fbtnc_696)
btnc_696.grid(row=0,column=0)
btnc_697 = Button(frmc_140, bg=list_c[696], font=("", 36), command=fbtnc_697)
btnc_697.grid(row=0,column=1)
btnc_698 = Button(frmc_140, bg=list_c[697], font=("", 36), command=fbtnc_698)
btnc_698.grid(row=0,column=2)
btnc_699 = Button(frmc_140, bg=list_c[698], font=("", 36), command=fbtnc_699)
btnc_699.grid(row=0,column=3)
btnc_700 = Button(frmc_140, bg=list_c[699], font=("", 36), command=fbtnc_700)
btnc_700.grid(row=0,column=4)

frmc_141 = Frame(big_frm6)
frmc_141.grid(row=3, column=0, padx=20)

btnc_701 = Button(frmc_141, bg=list_c[700], font=("", 36), command=fbtnc_701)
btnc_701.grid(row=0,column=0)
btnc_702 = Button(frmc_141, bg=list_c[701], font=("", 36), command=fbtnc_702)
btnc_702.grid(row=0,column=1)
btnc_703 = Button(frmc_141, bg=list_c[702], font=("", 36), command=fbtnc_703)
btnc_703.grid(row=0,column=2)
btnc_704 = Button(frmc_141, bg=list_c[703], font=("", 36), command=fbtnc_704)
btnc_704.grid(row=0,column=3)
btnc_705 = Button(frmc_141, bg=list_c[704], font=("", 36), command=fbtnc_705)
btnc_705.grid(row=0,column=4)

frmc_142 = Frame(big_frm6)
frmc_142.grid(row=3, column=1)

btnc_706 = Button(frmc_142, bg=list_c[705], font=("", 36), command=fbtnc_706)
btnc_706.grid(row=0,column=0)
btnc_707 = Button(frmc_142, bg=list_c[706], font=("", 36), command=fbtnc_707)
btnc_707.grid(row=0,column=1)
btnc_708 = Button(frmc_142, bg=list_c[707], font=("", 36), command=fbtnc_708)
btnc_708.grid(row=0,column=2)
btnc_709 = Button(frmc_142, bg=list_c[708], font=("", 36), command=fbtnc_709)
btnc_709.grid(row=0,column=3)
btnc_710 = Button(frmc_142, bg=list_c[709], font=("", 36), command=fbtnc_710)
btnc_710.grid(row=0,column=4)

frmc_143 = Frame(big_frm6)
frmc_143.grid(row=3, column=2, padx=20)

btnc_711 = Button(frmc_143, bg=list_c[710], font=("", 36), command=fbtnc_711)
btnc_711.grid(row=0,column=0)
btnc_712 = Button(frmc_143, bg=list_c[711], font=("", 36), command=fbtnc_712)
btnc_712.grid(row=0,column=1)
btnc_713 = Button(frmc_143, bg=list_c[712], font=("", 36), command=fbtnc_713)
btnc_713.grid(row=0,column=2)
btnc_714 = Button(frmc_143, bg=list_c[713], font=("", 36), command=fbtnc_714)
btnc_714.grid(row=0,column=3)
btnc_715 = Button(frmc_143, bg=list_c[714], font=("", 36), command=fbtnc_715)
btnc_715.grid(row=0,column=4)


frmc_144 = Frame(big_frm6)
frmc_144.grid(row=3, column=3)

btnc_716 = Button(frmc_144, bg=list_c[715], font=("", 36), command=fbtnc_716)
btnc_716.grid(row=0,column=0)
btnc_717 = Button(frmc_144, bg=list_c[716], font=("", 36), command=fbtnc_717)
btnc_717.grid(row=0,column=1)
btnc_718 = Button(frmc_144, bg=list_c[717], font=("", 36), command=fbtnc_718)
btnc_718.grid(row=0,column=2)
btnc_719 = Button(frmc_144, bg=list_c[718], font=("", 36), command=fbtnc_719)
btnc_719.grid(row=0,column=3)
btnc_720 = Button(frmc_144, bg=list_c[719], font=("", 36), command=fbtnc_720)
btnc_720.grid(row=0,column=4)

frmc_145 = Frame(big_frm6)
frmc_145.grid(row=3, column=4, padx=20)

btnc_721 = Button(frmc_145, bg=list_c[720], font=("", 36), command=fbtnc_721)
btnc_721.grid(row=0,column=0)
btnc_722 = Button(frmc_145, bg=list_c[721], font=("", 36), command=fbtnc_722)
btnc_722.grid(row=0,column=1)
btnc_723 = Button(frmc_145, bg=list_c[722], font=("", 36), command=fbtnc_723)
btnc_723.grid(row=0,column=2)
btnc_724 = Button(frmc_145, bg=list_c[723], font=("", 36), command=fbtnc_724)
btnc_724.grid(row=0,column=3)
btnc_725 = Button(frmc_145, bg=list_c[724], font=("", 36), command=fbtnc_725)
btnc_725.grid(row=0,column=4)

frmc_146 = Frame(big_frm6)
frmc_146.grid(row=4, column=0, padx=20)

btnc_726 = Button(frmc_146, bg=list_c[725], font=("", 36), command=fbtnc_726)
btnc_726.grid(row=0,column=0)
btnc_727 = Button(frmc_146, bg=list_c[726], font=("", 36), command=fbtnc_727)
btnc_727.grid(row=0,column=1)
btnc_728 = Button(frmc_146, bg=list_c[727], font=("", 36), command=fbtnc_728)
btnc_728.grid(row=0,column=2)
btnc_729 = Button(frmc_146, bg=list_c[728], font=("", 36), command=fbtnc_729)
btnc_729.grid(row=0,column=3)
btnc_730 = Button(frmc_146, bg=list_c[729], font=("", 36), command=fbtnc_730)
btnc_730.grid(row=0,column=4)

frmc_147 = Frame(big_frm6)
frmc_147.grid(row=4, column=1)

btnc_731 = Button(frmc_147, bg=list_c[730], font=("", 36), command=fbtnc_731)
btnc_731.grid(row=0,column=0)
btnc_732 = Button(frmc_147, bg=list_c[731], font=("", 36), command=fbtnc_732)
btnc_732.grid(row=0,column=1)
btnc_733 = Button(frmc_147, bg=list_c[732], font=("", 36), command=fbtnc_733)
btnc_733.grid(row=0,column=2)
btnc_734 = Button(frmc_147, bg=list_c[733], font=("", 36), command=fbtnc_734)
btnc_734.grid(row=0,column=3)
btnc_735 = Button(frmc_147, bg=list_c[734], font=("", 36), command=fbtnc_735)
btnc_735.grid(row=0,column=4)

frmc_148 = Frame(big_frm6)
frmc_148.grid(row=4, column=2, padx=20)

btnc_736 = Button(frmc_148, bg=list_c[735], font=("", 36), command=fbtnc_736)
btnc_736.grid(row=0,column=0)
btnc_737 = Button(frmc_148, bg=list_c[736], font=("", 36), command=fbtnc_737)
btnc_737.grid(row=0,column=1)
btnc_738 = Button(frmc_148, bg=list_c[737], font=("", 36), command=fbtnc_738)
btnc_738.grid(row=0,column=2)
btnc_739 = Button(frmc_148, bg=list_c[738], font=("", 36), command=fbtnc_739)
btnc_739.grid(row=0,column=3)
btnc_740 = Button(frmc_148, bg=list_c[739], font=("", 36), command=fbtnc_740)
btnc_740.grid(row=0,column=4)

frmc_149 = Frame(big_frm6)
frmc_149.grid(row=4, column=3)

btnc_741 = Button(frmc_149, bg=list_c[740], font=("", 36), command=fbtnc_741)
btnc_741.grid(row=0,column=0)
btnc_742 = Button(frmc_149, bg=list_c[741], font=("", 36), command=fbtnc_742)
btnc_742.grid(row=0,column=1)
btnc_743 = Button(frmc_149, bg=list_c[742], font=("", 36), command=fbtnc_743)
btnc_743.grid(row=0,column=2)
btnc_744 = Button(frmc_149, bg=list_c[743], font=("", 36), command=fbtnc_744)
btnc_744.grid(row=0,column=3)
btnc_745 = Button(frmc_149, bg=list_c[744], font=("", 36), command=fbtnc_745)
btnc_745.grid(row=0,column=4)

frmc_150 = Frame(big_frm6)
frmc_150.grid(row=4, column=4, padx=20, pady=20)

btnc_746 = Button(frmc_150, bg=list_c[745], font=("", 36), command=fbtnc_746)
btnc_746.grid(row=0,column=0)
btnc_747 = Button(frmc_150, bg=list_c[746], font=("", 36), command=fbtnc_747)
btnc_747.grid(row=0,column=1)
btnc_748 = Button(frmc_150, bg=list_c[747], font=("", 36), command=fbtnc_748)
btnc_748.grid(row=0,column=2)
btnc_749 = Button(frmc_150, bg=list_c[748], font=("", 36), command=fbtnc_749)
btnc_749.grid(row=0,column=3)
btnc_750 = Button(frmc_150, bg=list_c[749], font=("", 36), command=fbtnc_750)
btnc_750.grid(row=0,column=4)



#-------------------------------------------------------------------------------------------------------------

big_frm7 = Frame(root, bg="#f15bb5")

frmc_151 = Frame(big_frm7)
frmc_151.grid(row=0, column=0, padx=20)

btnc_751 = Button(frmc_151, bg=list_c[750], font=("", 36), command=fbtnc_751)
btnc_751.grid(row=0,column=0)
btnc_752 = Button(frmc_151, bg=list_c[751], font=("", 36), command=fbtnc_752)
btnc_752.grid(row=0,column=1)
btnc_753 = Button(frmc_151, bg=list_c[752], font=("", 36), command=fbtnc_753)
btnc_753.grid(row=0,column=2)
btnc_754 = Button(frmc_151, bg=list_c[753], font=("", 36), command=fbtnc_754)
btnc_754.grid(row=0,column=3)
btnc_755 = Button(frmc_151, bg=list_c[754], font=("", 36), command=fbtnc_755)
btnc_755.grid(row=0,column=4)

frmc_152 = Frame(big_frm7)
frmc_152.grid(row=0, column=1)

btnc_756 = Button(frmc_152, bg=list_c[755], font=("", 36), command=fbtnc_756)
btnc_756.grid(row=0,column=0)
btnc_757 = Button(frmc_152, bg=list_c[756], font=("", 36), command=fbtnc_757)
btnc_757.grid(row=0,column=1)
btnc_758 = Button(frmc_152, bg=list_c[757], font=("", 36), command=fbtnc_758)
btnc_758.grid(row=0,column=2)
btnc_759 = Button(frmc_152, bg=list_c[758], font=("", 36), command=fbtnc_759)
btnc_759.grid(row=0,column=3)
btnc_760 = Button(frmc_152, bg=list_c[759], font=("", 36), command=fbtnc_760)
btnc_760.grid(row=0,column=4)

frmc_153 = Frame(big_frm7)
frmc_153.grid(row=0, column=2, padx=20)

btnc_761 = Button(frmc_153, bg=list_c[760], font=("", 36), command=fbtnc_761)
btnc_761.grid(row=0,column=0)
btnc_762 = Button(frmc_153, bg=list_c[761], font=("", 36), command=fbtnc_762)
btnc_762.grid(row=0,column=1)
btnc_763 = Button(frmc_153, bg=list_c[762], font=("", 36), command=fbtnc_763)
btnc_763.grid(row=0,column=2)
btnc_764 = Button(frmc_153, bg=list_c[763], font=("", 36), command=fbtnc_764)
btnc_764.grid(row=0,column=3)
btnc_765 = Button(frmc_153, bg=list_c[764], font=("", 36), command=fbtnc_765)
btnc_765.grid(row=0,column=4)

frmc_154 = Frame(big_frm7)
frmc_154.grid(row=0, column=3)

btnc_766 = Button(frmc_154, bg=list_c[765], font=("", 36), command=fbtnc_766)
btnc_766.grid(row=0,column=0)
btnc_767 = Button(frmc_154, bg=list_c[766], font=("", 36), command=fbtnc_767)
btnc_767.grid(row=0,column=16)
btnc_768 = Button(frmc_154, bg=list_c[767], font=("", 36), command=fbtnc_768)
btnc_768.grid(row=0,column=2)
btnc_769 = Button(frmc_154, bg=list_c[768], font=("", 36), command=fbtnc_769)
btnc_769.grid(row=0,column=3)
btnc_770 = Button(frmc_154, bg=list_c[769], font=("", 36), command=fbtnc_770)
btnc_770.grid(row=0,column=4)

frmc_155 = Frame(big_frm7)
frmc_155.grid(row=0, column=4, padx=20, pady=20)

btnc_771 = Button(frmc_155, bg=list_c[770], font=("", 36), command=fbtnc_771)
btnc_771.grid(row=0,column=0)
btnc_772 = Button(frmc_155, bg=list_c[771], font=("", 36), command=fbtnc_772)
btnc_772.grid(row=0,column=1)
btnc_773 = Button(frmc_155, bg=list_c[772], font=("", 36), command=fbtnc_773)
btnc_773.grid(row=0,column=2)
btnc_774 = Button(frmc_155, bg=list_c[773], font=("", 36), command=fbtnc_774)
btnc_774.grid(row=0,column=3)
btnc_775 = Button(frmc_155, bg=list_c[774], font=("", 36), command=fbtnc_775)
btnc_775.grid(row=0,column=4)

frmc_156 = Frame(big_frm7)
frmc_156.grid(row=1, column=0, padx=20)

btnc_776 = Button(frmc_156, bg=list_c[775], font=("", 36), command=fbtnc_776)
btnc_776.grid(row=0,column=0)
btnc_777 = Button(frmc_156, bg=list_c[776], font=("", 36), command=fbtnc_777)
btnc_777.grid(row=0,column=1)
btnc_778 = Button(frmc_156, bg=list_c[777], font=("", 36), command=fbtnc_778)
btnc_778.grid(row=0,column=2)
btnc_779 = Button(frmc_156, bg=list_c[778], font=("", 36), command=fbtnc_779)
btnc_779.grid(row=0,column=3)
btnc_780 = Button(frmc_156, bg=list_c[779], font=("", 36), command=fbtnc_780)
btnc_780.grid(row=0,column=4)

frmc_157 = Frame(big_frm7)
frmc_157.grid(row=1, column=1)

btnc_781 = Button(frmc_157, bg=list_c[780], font=("", 36), command=fbtnc_781)
btnc_781.grid(row=0,column=0)
btnc_782 = Button(frmc_157, bg=list_c[781], font=("", 36), command=fbtnc_782)
btnc_782.grid(row=0,column=1)
btnc_783 = Button(frmc_157, bg=list_c[782], font=("", 36), command=fbtnc_783)
btnc_783.grid(row=0,column=2)
btnc_784 = Button(frmc_157, bg=list_c[783], font=("", 36), command=fbtnc_784)
btnc_784.grid(row=0,column=3)
btnc_785 = Button(frmc_157, bg=list_c[784], font=("", 36), command=fbtnc_785)
btnc_785.grid(row=0,column=4)

frmc_158 = Frame(big_frm7)
frmc_158.grid(row=1, column=2, padx=20)

btnc_786 = Button(frmc_158, bg=list_c[785], font=("", 36), command=fbtnc_786)
btnc_786.grid(row=0,column=0)
btnc_787 = Button(frmc_158, bg=list_c[786], font=("", 36), command=fbtnc_787)
btnc_787.grid(row=0,column=1)
btnc_788 = Button(frmc_158, bg=list_c[787], font=("", 36), command=fbtnc_788)
btnc_788.grid(row=0,column=2)
btnc_789 = Button(frmc_158, bg=list_c[788], font=("", 36), command=fbtnc_789)
btnc_789.grid(row=0,column=3)
btnc_790 = Button(frmc_158, bg=list_c[789], font=("", 36), command=fbtnc_790)
btnc_790.grid(row=0,column=4)

frmc_159 = Frame(big_frm7)
frmc_159.grid(row=1, column=3)

btnc_791 = Button(frmc_159, bg=list_c[790], font=("", 36), command=fbtnc_791)
btnc_791.grid(row=0,column=0)
btnc_792 = Button(frmc_159, bg=list_c[791], font=("", 36), command=fbtnc_792)
btnc_792.grid(row=0,column=1)
btnc_793 = Button(frmc_159, bg=list_c[792], font=("", 36), command=fbtnc_793)
btnc_793.grid(row=0,column=2)
btnc_794 = Button(frmc_159, bg=list_c[793], font=("", 36), command=fbtnc_794)
btnc_794.grid(row=0,column=3)
btnc_795 = Button(frmc_159, bg=list_c[794], font=("", 36), command=fbtnc_795)
btnc_795.grid(row=0,column=4)

frmc_160 = Frame(big_frm7)
frmc_160.grid(row=1, column=4, padx=20)

btnc_796 = Button(frmc_160, bg=list_c[795], font=("", 36), command=fbtnc_796)
btnc_796.grid(row=0,column=0)
btnc_797 = Button(frmc_160, bg=list_c[796], font=("", 36), command=fbtnc_797)
btnc_797.grid(row=0,column=1)
btnc_798 = Button(frmc_160, bg=list_c[797], font=("", 36), command=fbtnc_798)
btnc_798.grid(row=0,column=2)
btnc_799 = Button(frmc_160, bg=list_c[798], font=("", 36), command=fbtnc_799)
btnc_799.grid(row=0,column=3)
btnc_800 = Button(frmc_160, bg=list_c[799], font=("", 36), command=fbtnc_800)
btnc_800.grid(row=0,column=4)

frmc_161 = Frame(big_frm7)
frmc_161.grid(row=2, column=0, padx=20)

btnc_801 = Button(frmc_161, bg=list_c[800], font=("", 36), command=fbtnc_801)
btnc_801.grid(row=0,column=0)
btnc_802 = Button(frmc_161, bg=list_c[801], font=("", 36), command=fbtnc_802)
btnc_802.grid(row=0,column=1)
btnc_803 = Button(frmc_161, bg=list_c[802], font=("", 36), command=fbtnc_803)
btnc_803.grid(row=0,column=2)
btnc_804 = Button(frmc_161, bg=list_c[803], font=("", 36), command=fbtnc_804)
btnc_804.grid(row=0,column=3)
btnc_805 = Button(frmc_161, bg=list_c[804], font=("", 36), command=fbtnc_805)
btnc_805.grid(row=0,column=4)

frmc_162 = Frame(big_frm7)
frmc_162.grid(row=2, column=1)

btnc_806 = Button(frmc_162, bg=list_c[805], font=("", 36), command=fbtnc_806)
btnc_806.grid(row=0,column=0)
btnc_807 = Button(frmc_162, bg=list_c[806], font=("", 36), command=fbtnc_807)
btnc_807.grid(row=0,column=1)
btnc_808 = Button(frmc_162, bg=list_c[807], font=("", 36), command=fbtnc_808)
btnc_808.grid(row=0,column=2)
btnc_809 = Button(frmc_162, bg=list_c[808], font=("", 36), command=fbtnc_809)
btnc_809.grid(row=0,column=3)
btnc_810 = Button(frmc_162, bg=list_c[809], font=("", 36), command=fbtnc_810)
btnc_810.grid(row=0,column=4)

frmc_163 = Frame(big_frm7)
frmc_163.grid(row=2, column=2, padx=20)

btnc_811 = Button(frmc_163, bg=list_c[810], font=("", 36), command=fbtnc_811)
btnc_811.grid(row=0,column=0)
btnc_812 = Button(frmc_163, bg=list_c[811], font=("", 36), command=fbtnc_812)
btnc_812.grid(row=0,column=1)
btnc_813 = Button(frmc_163, bg=list_c[812], font=("", 36), command=fbtnc_813)
btnc_813.grid(row=0,column=2)
btnc_814 = Button(frmc_163, bg=list_c[813], font=("", 36), command=fbtnc_814)
btnc_814.grid(row=0,column=3)
btnc_815 = Button(frmc_163, bg=list_c[814], font=("", 36), command=fbtnc_815)
btnc_815.grid(row=0,column=4)

frmc_164 = Frame(big_frm7)
frmc_164.grid(row=2, column=3)

btnc_816 = Button(frmc_164, bg=list_c[815], font=("", 36), command=fbtnc_816)
btnc_816.grid(row=0,column=0)
btnc_817 = Button(frmc_164, bg=list_c[816], font=("", 36), command=fbtnc_817)
btnc_817.grid(row=0,column=1)
btnc_818 = Button(frmc_164, bg=list_c[817], font=("", 36), command=fbtnc_818)
btnc_818.grid(row=0,column=2)
btnc_819 = Button(frmc_164, bg=list_c[818], font=("", 36), command=fbtnc_819)
btnc_819.grid(row=0,column=3)
btnc_820 = Button(frmc_164, bg=list_c[819], font=("", 36), command=fbtnc_820)
btnc_820.grid(row=0,column=4)

frmc_165 = Frame(big_frm7)
frmc_165.grid(row=2, column=4, padx=20, pady=20)

btnc_821 = Button(frmc_165, bg=list_c[820], font=("", 36), command=fbtnc_821)
btnc_821.grid(row=0,column=0)
btnc_822 = Button(frmc_165, bg=list_c[821], font=("", 36), command=fbtnc_822)
btnc_822.grid(row=0,column=1)
btnc_823 = Button(frmc_165, bg=list_c[822], font=("", 36), command=fbtnc_823)
btnc_823.grid(row=0,column=2)
btnc_824 = Button(frmc_165, bg=list_c[823], font=("", 36), command=fbtnc_824)
btnc_824.grid(row=0,column=3)
btnc_825 = Button(frmc_165, bg=list_c[824], font=("", 36), command=fbtnc_825)
btnc_825.grid(row=0,column=4)

frmc_166 = Frame(big_frm7)
frmc_166.grid(row=3, column=0, padx=20)

btnc_826 = Button(frmc_166, bg=list_c[825], font=("", 36), command=fbtnc_826)
btnc_826.grid(row=0,column=0)
btnc_827 = Button(frmc_166, bg=list_c[826], font=("", 36), command=fbtnc_827)
btnc_827.grid(row=0,column=1)
btnc_828 = Button(frmc_166, bg=list_c[827], font=("", 36), command=fbtnc_828)
btnc_828.grid(row=0,column=2)
btnc_829 = Button(frmc_166, bg=list_c[828], font=("", 36), command=fbtnc_829)
btnc_829.grid(row=0,column=3)
btnc_830 = Button(frmc_166, bg=list_c[829], font=("", 36), command=fbtnc_830)
btnc_830.grid(row=0,column=4)

frmc_167 = Frame(big_frm7)
frmc_167.grid(row=3, column=1)

btnc_831 = Button(frmc_167, bg=list_c[830], font=("", 36), command=fbtnc_831)
btnc_831.grid(row=0,column=0)
btnc_832 = Button(frmc_167, bg=list_c[831], font=("", 36), command=fbtnc_832)
btnc_832.grid(row=0,column=1)
btnc_833 = Button(frmc_167, bg=list_c[832], font=("", 36), command=fbtnc_833)
btnc_833.grid(row=0,column=2)
btnc_834 = Button(frmc_167, bg=list_c[833], font=("", 36), command=fbtnc_834)
btnc_834.grid(row=0,column=3)
btnc_835 = Button(frmc_167, bg=list_c[834], font=("", 36), command=fbtnc_835)
btnc_835.grid(row=0,column=4)

frmc_168 = Frame(big_frm7)
frmc_168.grid(row=3, column=2, padx=20)

btnc_836 = Button(frmc_168, bg=list_c[835], font=("", 36), command=fbtnc_836)
btnc_836.grid(row=0,column=0)
btnc_837 = Button(frmc_168, bg=list_c[836], font=("", 36), command=fbtnc_837)
btnc_837.grid(row=0,column=1)
btnc_838 = Button(frmc_168, bg=list_c[837], font=("", 36), command=fbtnc_838)
btnc_838.grid(row=0,column=2)
btnc_839 = Button(frmc_168, bg=list_c[838], font=("", 36), command=fbtnc_839)
btnc_839.grid(row=0,column=3)
btnc_840 = Button(frmc_168, bg=list_c[839], font=("", 36), command=fbtnc_840)
btnc_840.grid(row=0,column=4)

frmc_169 = Frame(big_frm7)
frmc_169.grid(row=3, column=3)

btnc_841 = Button(frmc_169, bg=list_c[840], font=("", 36), command=fbtnc_841)
btnc_841.grid(row=0,column=0)
btnc_842 = Button(frmc_169, bg=list_c[841], font=("", 36), command=fbtnc_842)
btnc_842.grid(row=0,column=1)
btnc_843 = Button(frmc_169, bg=list_c[842], font=("", 36), command=fbtnc_843)
btnc_843.grid(row=0,column=2)
btnc_844 = Button(frmc_169, bg=list_c[843], font=("", 36), command=fbtnc_844)
btnc_844.grid(row=0,column=3)
btnc_845 = Button(frmc_169, bg=list_c[844], font=("", 36), command=fbtnc_845)
btnc_845.grid(row=0,column=4)

frmc_170 = Frame(big_frm7)
frmc_170.grid(row=3, column=4, padx=20)

btnc_846 = Button(frmc_170, bg=list_c[845], font=("", 36), command=fbtnc_846)
btnc_846.grid(row=0,column=0)
btnc_847 = Button(frmc_170, bg=list_c[846], font=("", 36), command=fbtnc_847)
btnc_847.grid(row=0,column=1)
btnc_848 = Button(frmc_170, bg=list_c[847], font=("", 36), command=fbtnc_848)
btnc_848.grid(row=0,column=2)
btnc_849 = Button(frmc_170, bg=list_c[848], font=("", 36), command=fbtnc_849)
btnc_849.grid(row=0,column=3)
btnc_850 = Button(frmc_170, bg=list_c[849], font=("", 36), command=fbtnc_850)
btnc_850.grid(row=0,column=4)

frmc_171 = Frame(big_frm7)
frmc_171.grid(row=4, column=0, padx=20)

btnc_851 = Button(frmc_171, bg=list_c[850], font=("", 36), command=fbtnc_851)
btnc_851.grid(row=0,column=0)
btnc_852 = Button(frmc_171, bg=list_c[851], font=("", 36), command=fbtnc_852)
btnc_852.grid(row=0,column=1)
btnc_853 = Button(frmc_171, bg=list_c[852], font=("", 36), command=fbtnc_853)
btnc_853.grid(row=0,column=2)
btnc_854 = Button(frmc_171, bg=list_c[853], font=("", 36), command=fbtnc_854)
btnc_854.grid(row=0,column=3)
btnc_855 = Button(frmc_171, bg=list_c[854], font=("", 36), command=fbtnc_855)
btnc_855.grid(row=0,column=4)

frmc_172 = Frame(big_frm7)
frmc_172.grid(row=4, column=1)

btnc_856 = Button(frmc_172, bg=list_c[855], font=("", 36), command=fbtnc_856)
btnc_856.grid(row=0,column=0)
btnc_857 = Button(frmc_172, bg=list_c[856], font=("", 36), command=fbtnc_857)
btnc_857.grid(row=0,column=1)
btnc_858 = Button(frmc_172, bg=list_c[857], font=("", 36), command=fbtnc_858)
btnc_858.grid(row=0,column=2)
btnc_859 = Button(frmc_172, bg=list_c[858], font=("", 36), command=fbtnc_859)
btnc_859.grid(row=0,column=3)
btnc_850 = Button(frmc_172, bg=list_c[859], font=("", 36), command=fbtnc_860)
btnc_850.grid(row=0,column=4)

frmc_173 = Frame(big_frm7)
frmc_173.grid(row=4, column=2, padx=20)

btnc_861 = Button(frmc_173, bg=list_c[860], font=("", 36), command=fbtnc_861)
btnc_861.grid(row=0,column=0)
btnc_862 = Button(frmc_173, bg=list_c[861], font=("", 36), command=fbtnc_862)
btnc_862.grid(row=0,column=1)
btnc_863 = Button(frmc_173, bg=list_c[862], font=("", 36), command=fbtnc_863)
btnc_863.grid(row=0,column=2)
btnc_864 = Button(frmc_173, bg=list_c[863], font=("", 36), command=fbtnc_864)
btnc_864.grid(row=0,column=3)
btnc_865 = Button(frmc_173, bg=list_c[864], font=("", 36), command=fbtnc_865)
btnc_865.grid(row=0,column=4)

frmc_174 = Frame(big_frm7)
frmc_174.grid(row=4, column=3)

btnc_866 = Button(frmc_174, bg=list_c[865], font=("", 36), command=fbtnc_866)
btnc_866.grid(row=0,column=0)
btnc_867 = Button(frmc_174, bg=list_c[866], font=("", 36), command=fbtnc_867)
btnc_867.grid(row=0,column=1)
btnc_868 = Button(frmc_174, bg=list_c[867], font=("", 36), command=fbtnc_868)
btnc_868.grid(row=0,column=2)
btnc_869 = Button(frmc_174, bg=list_c[868], font=("", 36), command=fbtnc_869)
btnc_869.grid(row=0,column=3)
btnc_870 = Button(frmc_174, bg=list_c[869], font=("", 36), command=fbtnc_870)
btnc_870.grid(row=0,column=4)

frmc_175 = Frame(big_frm7)
frmc_175.grid(row=4, column=4, padx=20, pady=20)

btnc_871 = Button(frmc_175, bg=list_c[870], font=("", 36), command=fbtnc_871)
btnc_871.grid(row=0,column=0)
btnc_872 = Button(frmc_175, bg=list_c[871], font=("", 36), command=fbtnc_872)
btnc_872.grid(row=0,column=1)
btnc_873 = Button(frmc_175, bg=list_c[872], font=("", 36), command=fbtnc_873)
btnc_873.grid(row=0,column=2)
btnc_874 = Button(frmc_175, bg=list_c[873], font=("", 36), command=fbtnc_874)
btnc_874.grid(row=0,column=3)
btnc_875 = Button(frmc_175, bg=list_c[874], font=("", 36), command=fbtnc_875)
btnc_875.grid(row=0,column=4)



#----------------------------------------------------------------------------------------------------------------------



big_frm8 = Frame(root, bg="#f15bb5")

frmc_176 = Frame(big_frm8)
frmc_176.grid(row=0, column=0, padx=20)

btnc_876 = Button(frmc_176, bg=list_c[875], font=("", 36), command=fbtnc_886)
btnc_876.grid(row=0,column=0)
btnc_877 = Button(frmc_176, bg=list_c[876], font=("", 36), command=fbtnc_887)
btnc_877.grid(row=0,column=1)
btnc_878 = Button(frmc_176, bg=list_c[877], font=("", 36), command=fbtnc_888)
btnc_878.grid(row=0,column=2)
btnc_879 = Button(frmc_176, bg=list_c[878], font=("", 36), command=fbtnc_889)
btnc_879.grid(row=0,column=3)
btnc_880 = Button(frmc_176, bg=list_c[879], font=("", 36), command=fbtnc_880)
btnc_880.grid(row=0,column=4)

frmc_177 = Frame(big_frm8)
frmc_177.grid(row=0, column=1)

btnc_881 = Button(frmc_177, bg=list_c[880], font=("", 36), command=fbtnc_881)
btnc_881.grid(row=0,column=0)
btnc_882 = Button(frmc_177, bg=list_c[881], font=("", 36), command=fbtnc_882)
btnc_882.grid(row=0,column=1)
btnc_883 = Button(frmc_177, bg=list_c[882], font=("", 36), command=fbtnc_883)
btnc_883.grid(row=0,column=2)
btnc_884 = Button(frmc_177, bg=list_c[883], font=("", 36), command=fbtnc_884)
btnc_884.grid(row=0,column=3)
btnc_885 = Button(frmc_177, bg=list_c[884], font=("", 36), command=fbtnc_885)
btnc_885.grid(row=0,column=4)

frmc_178 = Frame(big_frm8)
frmc_178.grid(row=0, column=2, padx=20)

btnc_886 = Button(frmc_178, bg=list_c[885], font=("", 36), command=fbtnc_886)
btnc_886.grid(row=0,column=0)
btnc_887 = Button(frmc_178, bg=list_c[886], font=("", 36), command=fbtnc_887)
btnc_887.grid(row=0,column=1)
btnc_888 = Button(frmc_178, bg=list_c[887], font=("", 36), command=fbtnc_888)
btnc_888.grid(row=0,column=2)
btnc_889 = Button(frmc_178, bg=list_c[888], font=("", 36), command=fbtnc_889)
btnc_889.grid(row=0,column=3)
btnc_890 = Button(frmc_178, bg=list_c[889], font=("", 36), command=fbtnc_890)
btnc_890.grid(row=0,column=4)

frmc_179 = Frame(big_frm8)
frmc_179.grid(row=0, column=3)

btnc_891 = Button(frmc_179, bg=list_c[890], font=("", 36), command=fbtnc_891)
btnc_891.grid(row=0,column=0)
btnc_892 = Button(frmc_179, bg=list_c[891], font=("", 36), command=fbtnc_892)
btnc_892.grid(row=0,column=1)
btnc_893 = Button(frmc_179, bg=list_c[892], font=("", 36), command=fbtnc_893)
btnc_893.grid(row=0,column=2)
btnc_894 = Button(frmc_179, bg=list_c[893], font=("", 36), command=fbtnc_894)
btnc_894.grid(row=0,column=3)
btnc_895 = Button(frmc_179, bg=list_c[894], font=("", 36), command=fbtnc_895)
btnc_895.grid(row=0,column=4)

frmc_180 = Frame(big_frm8)
frmc_180.grid(row=0, column=4, padx=20, pady=20)

btnc_896 = Button(frmc_180, bg=list_c[895], font=("", 36), command=fbtnc_896)
btnc_896.grid(row=0,column=0)
btnc_897 = Button(frmc_180, bg=list_c[896], font=("", 36), command=fbtnc_897)
btnc_897.grid(row=0,column=1)
btnc_898 = Button(frmc_180, bg=list_c[897], font=("", 36), command=fbtnc_898)
btnc_898.grid(row=0,column=2)
btnc_899 = Button(frmc_180, bg=list_c[898], font=("", 36), command=fbtnc_899)
btnc_899.grid(row=0,column=3)
btnc_900 = Button(frmc_180, bg=list_c[899], font=("", 36), command=fbtnc_900)
btnc_900.grid(row=0,column=4)

frmc_181 = Frame(big_frm8)
frmc_181.grid(row=1, column=0, padx=20)

btnc_901 = Button(frmc_181, bg=list_c[900], font=("", 36), command=fbtnc_901)
btnc_901.grid(row=0,column=0)
btnc_902 = Button(frmc_181, bg=list_c[901], font=("", 36), command=fbtnc_902)
btnc_902.grid(row=0,column=1)
btnc_903 = Button(frmc_181, bg=list_c[902], font=("", 36), command=fbtnc_903)
btnc_903.grid(row=0,column=2)
btnc_904 = Button(frmc_181, bg=list_c[903], font=("", 36), command=fbtnc_904)
btnc_904.grid(row=0,column=3)
btnc_905 = Button(frmc_181, bg=list_c[904], font=("", 36), command=fbtnc_905)
btnc_905.grid(row=0,column=4)

frmc_182 = Frame(big_frm8)
frmc_182.grid(row=1, column=1)

btnc_906 = Button(frmc_182, bg=list_c[905], font=("", 36), command=fbtnc_906)
btnc_906.grid(row=0,column=0)
btnc_907 = Button(frmc_182, bg=list_c[906], font=("", 36), command=fbtnc_907)
btnc_907.grid(row=0,column=1)
btnc_908 = Button(frmc_182, bg=list_c[907], font=("", 36), command=fbtnc_908)
btnc_908.grid(row=0,column=2)
btnc_909 = Button(frmc_182, bg=list_c[908], font=("", 36), command=fbtnc_909)
btnc_909.grid(row=0,column=3)
btnc_910 = Button(frmc_182, bg=list_c[909], font=("", 36), command=fbtnc_910)
btnc_910.grid(row=0,column=4)

frmc_183 = Frame(big_frm8)
frmc_183.grid(row=1, column=2, padx=20)

btnc_911 = Button(frmc_183, bg=list_c[910], font=("", 36), command=fbtnc_911)
btnc_911.grid(row=0,column=0)
btnc_912 = Button(frmc_183, bg=list_c[911], font=("", 36), command=fbtnc_912)
btnc_912.grid(row=0,column=1)
btnc_913 = Button(frmc_183, bg=list_c[912], font=("", 36), command=fbtnc_913)
btnc_913.grid(row=0,column=2)
btnc_914 = Button(frmc_183, bg=list_c[913], font=("", 36), command=fbtnc_914)
btnc_914.grid(row=0,column=3)
btnc_915 = Button(frmc_183, bg=list_c[914], font=("", 36), command=fbtnc_915)
btnc_915.grid(row=0,column=4)

frmc_184 = Frame(big_frm8)
frmc_184.grid(row=1, column=3)

btnc_916 = Button(frmc_184, bg=list_c[915], font=("", 36), command=fbtnc_916)
btnc_916.grid(row=0,column=0)
btnc_917 = Button(frmc_184, bg=list_c[916], font=("", 36), command=fbtnc_917)
btnc_917.grid(row=0,column=1)
btnc_918 = Button(frmc_184, bg=list_c[917], font=("", 36), command=fbtnc_918)
btnc_918.grid(row=0,column=2)
btnc_919 = Button(frmc_184, bg=list_c[918], font=("", 36), command=fbtnc_919)
btnc_919.grid(row=0,column=3)
btnc_920 = Button(frmc_184, bg=list_c[919], font=("", 36), command=fbtnc_920)
btnc_920.grid(row=0,column=4)

frmc_185 = Frame(big_frm8)
frmc_185.grid(row=1, column=4, padx=20)

btnc_921 = Button(frmc_185, bg=list_c[920], font=("", 36), command=fbtnc_921)
btnc_921.grid(row=0,column=0)
btnc_922 = Button(frmc_185, bg=list_c[921], font=("", 36), command=fbtnc_922)
btnc_922.grid(row=0,column=1)
btnc_923 = Button(frmc_185, bg=list_c[922], font=("", 36), command=fbtnc_923)
btnc_923.grid(row=0,column=2)
btnc_924 = Button(frmc_185, bg=list_c[923], font=("", 36), command=fbtnc_924)
btnc_924.grid(row=0,column=3)
btnc_925 = Button(frmc_185, bg=list_c[924], font=("", 36), command=fbtnc_925)
btnc_925.grid(row=0,column=4)

frmc_186 = Frame(big_frm8)
frmc_186.grid(row=2, column=0, padx=20)

btnc_926 = Button(frmc_186, bg=list_c[925], font=("", 36), command=fbtnc_926)
btnc_926.grid(row=0,column=0)
btnc_927 = Button(frmc_186, bg=list_c[926], font=("", 36), command=fbtnc_927)
btnc_927.grid(row=0,column=1)
btnc_928 = Button(frmc_186, bg=list_c[927], font=("", 36), command=fbtnc_928)
btnc_928.grid(row=0,column=2)
btnc_929 = Button(frmc_186, bg=list_c[928], font=("", 36), command=fbtnc_929)
btnc_929.grid(row=0,column=3)
btnc_930 = Button(frmc_186, bg=list_c[929], font=("", 36), command=fbtnc_930)
btnc_930.grid(row=0,column=4)

frmc_187 = Frame(big_frm8)
frmc_187.grid(row=2, column=1)

btnc_931 = Button(frmc_187, bg=list_c[930], font=("", 36), command=fbtnc_931)
btnc_931.grid(row=0,column=0)
btnc_932 = Button(frmc_187, bg=list_c[931], font=("", 36), command=fbtnc_932)
btnc_932.grid(row=0,column=1)
btnc_933 = Button(frmc_187, bg=list_c[932], font=("", 36), command=fbtnc_933)
btnc_933.grid(row=0,column=2)
btnc_934 = Button(frmc_187, bg=list_c[933], font=("", 36), command=fbtnc_934)
btnc_934.grid(row=0,column=3)
btnc_935 = Button(frmc_187, bg=list_c[934], font=("", 36), command=fbtnc_935)
btnc_935.grid(row=0,column=4)

frmc_188 = Frame(big_frm8)
frmc_188.grid(row=2, column=2, padx=20)

btnc_936 = Button(frmc_188, bg=list_c[935], font=("", 36), command=fbtnc_936)
btnc_936.grid(row=0,column=0)
btnc_937 = Button(frmc_188, bg=list_c[936], font=("", 36), command=fbtnc_937)
btnc_937.grid(row=0,column=1)
btnc_938 = Button(frmc_188, bg=list_c[937], font=("", 36), command=fbtnc_938)
btnc_938.grid(row=0,column=2)
btnc_939 = Button(frmc_188, bg=list_c[938], font=("", 36), command=fbtnc_939)
btnc_939.grid(row=0,column=3)
btnc_940 = Button(frmc_188, bg=list_c[939], font=("", 36), command=fbtnc_940)
btnc_940.grid(row=0,column=4)

frmc_189 = Frame(big_frm8)
frmc_189.grid(row=2, column=3)

btnc_941 = Button(frmc_189, bg=list_c[940], font=("", 36), command=fbtnc_941)
btnc_941.grid(row=0,column=0)
btnc_942 = Button(frmc_189, bg=list_c[941], font=("", 36), command=fbtnc_942)
btnc_942.grid(row=0,column=1)
btnc_943 = Button(frmc_189, bg=list_c[942], font=("", 36), command=fbtnc_943)
btnc_943.grid(row=0,column=2)
btnc_944 = Button(frmc_189, bg=list_c[943], font=("", 36), command=fbtnc_944)
btnc_944.grid(row=0,column=3)
btnc_945 = Button(frmc_189, bg=list_c[944], font=("", 36), command=fbtnc_945)
btnc_945.grid(row=0,column=4)

frmc_190 = Frame(big_frm8)
frmc_190.grid(row=2, column=4, padx=20, pady=20)

btnc_946 = Button(frmc_190, bg=list_c[945], font=("", 36), command=fbtnc_946)
btnc_946.grid(row=0,column=0)
btnc_947 = Button(frmc_190, bg=list_c[946], font=("", 36), command=fbtnc_947)
btnc_947.grid(row=0,column=1)
btnc_948 = Button(frmc_190, bg=list_c[947], font=("", 36), command=fbtnc_948)
btnc_948.grid(row=0,column=2)
btnc_949 = Button(frmc_190, bg=list_c[948], font=("", 36), command=fbtnc_949)
btnc_949.grid(row=0,column=3)
btnc_950 = Button(frmc_190, bg=list_c[949], font=("", 36), command=fbtnc_950)
btnc_950.grid(row=0,column=4)

frmc_191 = Frame(big_frm8)
frmc_191.grid(row=3, column=0, padx=20)

btnc_951 = Button(frmc_191, bg=list_c[950], font=("", 36), command=fbtnc_951)
btnc_951.grid(row=0,column=0)
btnc_952 = Button(frmc_191, bg=list_c[951], font=("", 36), command=fbtnc_952)
btnc_952.grid(row=0,column=1)
btnc_953 = Button(frmc_191, bg=list_c[952], font=("", 36), command=fbtnc_953)
btnc_953.grid(row=0,column=2)
btnc_954 = Button(frmc_191, bg=list_c[953], font=("", 36), command=fbtnc_954)
btnc_954.grid(row=0,column=3)
btnc_955 = Button(frmc_191, bg=list_c[954], font=("", 36), command=fbtnc_955)
btnc_955.grid(row=0,column=4)

frmc_192 = Frame(big_frm8)
frmc_192.grid(row=3, column=1)

btnc_956 = Button(frmc_192, bg=list_c[955], font=("", 36), command=fbtnc_956)
btnc_956.grid(row=0,column=0)
btnc_957 = Button(frmc_192, bg=list_c[956], font=("", 36), command=fbtnc_957)
btnc_957.grid(row=0,column=1)
btnc_958 = Button(frmc_192, bg=list_c[957], font=("", 36), command=fbtnc_958)
btnc_958.grid(row=0,column=2)
btnc_959 = Button(frmc_192, bg=list_c[958], font=("", 36), command=fbtnc_959)
btnc_959.grid(row=0,column=3)
btnc_960 = Button(frmc_192, bg=list_c[959], font=("", 36), command=fbtnc_960)
btnc_960.grid(row=0,column=4)

frmc_193 = Frame(big_frm8)
frmc_193.grid(row=3, column=2, padx=20)

btnc_961 = Button(frmc_193, bg=list_c[960], font=("", 36), command=fbtnc_961)
btnc_961.grid(row=0,column=0)
btnc_962 = Button(frmc_193, bg=list_c[961], font=("", 36), command=fbtnc_962)
btnc_962.grid(row=0,column=1)
btnc_963 = Button(frmc_193, bg=list_c[962], font=("", 36), command=fbtnc_963)
btnc_963.grid(row=0,column=2)
btnc_964 = Button(frmc_193, bg=list_c[963], font=("", 36), command=fbtnc_964)
btnc_964.grid(row=0,column=3)
btnc_965 = Button(frmc_193, bg=list_c[964], font=("", 36), command=fbtnc_965)
btnc_965.grid(row=0,column=4)

frmc_194 = Frame(big_frm8)
frmc_194.grid(row=3, column=3)

btnc_966 = Button(frmc_194, bg=list_c[965], font=("", 36), command=fbtnc_966)
btnc_966.grid(row=0,column=0)
btnc_967 = Button(frmc_194, bg=list_c[966], font=("", 36), command=fbtnc_967)
btnc_967.grid(row=0,column=1)
btnc_968 = Button(frmc_194, bg=list_c[967], font=("", 36), command=fbtnc_968)
btnc_968.grid(row=0,column=2)
btnc_969 = Button(frmc_194, bg=list_c[968], font=("", 36), command=fbtnc_969)
btnc_969.grid(row=0,column=3)
btnc_970 = Button(frmc_194, bg=list_c[969], font=("", 36), command=fbtnc_970)
btnc_970.grid(row=0,column=4)

frmc_195 = Frame(big_frm8)
frmc_195.grid(row=3, column=4, padx=20)

btnc_971 = Button(frmc_195, bg=list_c[970], font=("", 36), command=fbtnc_971)
btnc_971.grid(row=0,column=0)
btnc_972 = Button(frmc_195, bg=list_c[971], font=("", 36), command=fbtnc_972)
btnc_972.grid(row=0,column=1)
btnc_973 = Button(frmc_195, bg=list_c[972], font=("", 36), command=fbtnc_973)
btnc_973.grid(row=0,column=2)
btnc_974 = Button(frmc_195, bg=list_c[973], font=("", 36), command=fbtnc_974)
btnc_974.grid(row=0,column=3)
btnc_975 = Button(frmc_195, bg=list_c[974], font=("", 36), command=fbtnc_975)
btnc_975.grid(row=0,column=4)

frmc_196 = Frame(big_frm8)
frmc_196.grid(row=4, column=0, padx=20)

btnc_976 = Button(frmc_196, bg=list_c[975], font=("", 36), command=fbtnc_976)
btnc_976.grid(row=0,column=0)
btnc_977 = Button(frmc_196, bg=list_c[976], font=("", 36), command=fbtnc_977)
btnc_977.grid(row=0,column=1)
btnc_978 = Button(frmc_196, bg=list_c[977], font=("", 36), command=fbtnc_978)
btnc_978.grid(row=0,column=2)
btnc_979 = Button(frmc_196, bg=list_c[978], font=("", 36), command=fbtnc_979)
btnc_979.grid(row=0,column=3)
btnc_980 = Button(frmc_196, bg=list_c[979], font=("", 36), command=fbtnc_980)
btnc_980.grid(row=0,column=4)

frmc_197 = Frame(big_frm8)
frmc_197.grid(row=4, column=1)

btnc_981 = Button(frmc_197, bg=list_c[980], font=("", 36), command=fbtnc_981)
btnc_981.grid(row=0,column=0)
btnc_982 = Button(frmc_197, bg=list_c[981], font=("", 36), command=fbtnc_982)
btnc_982.grid(row=0,column=1)
btnc_983 = Button(frmc_197, bg=list_c[982], font=("", 36), command=fbtnc_983)
btnc_983.grid(row=0,column=2)
btnc_984 = Button(frmc_197, bg=list_c[983], font=("", 36), command=fbtnc_984)
btnc_984.grid(row=0,column=3)
btnc_985 = Button(frmc_197, bg=list_c[984], font=("", 36), command=fbtnc_985)
btnc_985.grid(row=0,column=4)

frmc_198 = Frame(big_frm8)
frmc_198.grid(row=4, column=2, padx=20)

btnc_986 = Button(frmc_198, bg=list_c[985], font=("", 36), command=fbtnc_986)
btnc_986.grid(row=0,column=0)
btnc_987 = Button(frmc_198, bg=list_c[986], font=("", 36), command=fbtnc_987)
btnc_987.grid(row=0,column=1)
btnc_988 = Button(frmc_198, bg=list_c[987], font=("", 36), command=fbtnc_988)
btnc_988.grid(row=0,column=2)
btnc_989 = Button(frmc_198, bg=list_c[988], font=("", 36), command=fbtnc_989)
btnc_989.grid(row=0,column=3)
btnc_990 = Button(frmc_198, bg=list_c[989], font=("", 36), command=fbtnc_990)
btnc_990.grid(row=0,column=4)

frmc_199 = Frame(big_frm8)
frmc_199.grid(row=4, column=3)

btnc_991 = Button(frmc_199, bg=list_c[990], font=("", 36), command=fbtnc_991)
btnc_991.grid(row=0,column=0)
btnc_992 = Button(frmc_199, bg=list_c[991], font=("", 36), command=fbtnc_992)
btnc_992.grid(row=0,column=1)
btnc_993 = Button(frmc_199, bg=list_c[992], font=("", 36), command=fbtnc_993)
btnc_993.grid(row=0,column=2)
btnc_994 = Button(frmc_199, bg=list_c[993], font=("", 36), command=fbtnc_994)
btnc_994.grid(row=0,column=3)
btnc_995 = Button(frmc_199, bg=list_c[994], font=("", 36), command=fbtnc_995)
btnc_995.grid(row=0,column=4)

frmc_200 = Frame(big_frm8)
frmc_200.grid(row=4, column=4, padx=20, pady=20)

btnc_996 = Button(frmc_200, bg=list_c[995], font=("", 36), command=fbtnc_996)
btnc_996.grid(row=0,column=0)
btnc_997 = Button(frmc_200, bg=list_c[996], font=("", 36), command=fbtnc_997)
btnc_997.grid(row=0,column=1)
btnc_998 = Button(frmc_200, bg=list_c[997], font=("", 36), command=fbtnc_998)
btnc_998.grid(row=0,column=2)
btnc_999 = Button(frmc_200, bg=list_c[998], font=("", 36), command=fbtnc_999)
btnc_999.grid(row=0,column=3)
btnc_1000 = Button(frmc_200, bg=list_c[999], font=("", 36), command=fbtnc_1000)
btnc_1000.grid(row=0,column=4)


list_bigfrm = [
    big_frm,
    big_frm2,
    big_frm3,
    big_frm4,
    big_frm5,
    big_frm6,
    big_frm7,
    big_frm8
]

root.mainloop()

