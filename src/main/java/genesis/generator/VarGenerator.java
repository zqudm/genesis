// Copyright (C) 2016 Fan Long, Peter Amidon, Martin Rianrd and MIT CSAIL 
// Genesis (A successor of Prophet for Java Programs)
// 
// This file is part of Genesis.
// 
// Genesis is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 2 of the License, or
// (at your option) any later version.
// 
// Genesis is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
// 
// You should have received a copy of the GNU General Public License
// along with Genesis.  If not, see <http://www.gnu.org/licenses/>.
package genesis.generator;

import java.util.ArrayList;

import genesis.node.MyCtNode;
import genesis.schema.VarTypeContext;
import spoon.reflect.factory.Factory;

public abstract class VarGenerator {

	public abstract ArrayList<MyCtNode> generate(MyCtNode before, Factory f, VarTypeContext context);

	public abstract boolean covers(MyCtNode before, MyCtNode after, VarTypeContext context);

	public abstract long estimateCost(MyCtNode before);

	public abstract boolean generatorEquals(VarGenerator g);
}