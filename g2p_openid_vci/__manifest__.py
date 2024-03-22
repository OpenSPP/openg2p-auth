# Part of OpenG2P Registry. See LICENSE file for full copyright and licensing details.
{
    "name": "G2P OpenID VCI: Base",
    "category": "G2P",
    "version": "15.0.1.2.0",
    "sequence": 1,
    "author": "OpenG2P",
    "website": "https://openg2p.org",
    "license": "Other OSI approved licence",
    "development_status": "Alpha",
    "depends": [
        "g2p_registry_base",
        "g2p_encryption",
    ],
    "external_dependencies": {"python": ["cryptography", "python-jose"]},
    "data": [
        "security/ir.model.access.csv",
        "views/vci_issuers.xml",
    ],
    "assets": {
        "web.assets_backend": [],
        "web.assets_qweb": [],
    },
    "demo": [],
    "images": [],
    "application": False,
    "installable": True,
    "auto_install": False,
}
