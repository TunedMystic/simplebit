DROP TABLE IF EXISTS "crypto";
CREATE TABLE "crypto" (
	"id" INTEGER PRIMARY KEY autoincrement,
	"name" VARCHAR(255) NOT NULL,
	"symbol" VARCHAR(255) NOT NULL,
    "asset_hash" VARCHAR(255),
	"category" INTEGER NOT NULL,
	"logo" VARCHAR(255),
	"description" TEXT,
    "website" VARCHAR(255),
	"platform" VARCHAR(255),
	"platform_token_address" VARCHAR(255),
    unique("name", "symbol")
);
